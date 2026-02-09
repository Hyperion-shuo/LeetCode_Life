这份回答旨在帮助你在面试中展示**代码规范性（Type Hinting）**、**张量操作熟练度（Einops）**以及对**核心算法逻辑**的清晰理解。

面试手写代码（Coding on Whiteboard/Pad）不同于工程落地，重点在于：**输入输出维度清晰**、**核心公式还原准确**、**变量命名易读**。

以下是基于 `torch` + `jaxtyping` + `einops` 的参考实现。

---

### 0. 基础环境与导入
向面试官说明：为了代码清晰，我使用了 `jaxtyping` 做类型标注，`einops` 处理维度。

```python
import torch
import torch.nn.functional as F
from jaxtyping import Float, Int
from torch import Tensor
from einops import reduce, rearrange
```

---

### 1. DPO Loss (Direct Preference Optimization)

**核心点**：DPO 不需要 Critic，直接优化 Policy 和 Reference Policy 之间的 Log 似然比（Log-likelihood Ratio）。
**公式**：$L_{DPO} = -\log \sigma (\beta (\log \frac{\pi_\theta(y_w)}{\pi_{ref}(y_w)} - \log \frac{\pi_\theta(y_l)}{\pi_{ref}(y_l)}))$

```python
def dpo_loss(
    policy_chosen_logps: Float[Tensor, "batch"],
    policy_rejected_logps: Float[Tensor, "batch"],
    ref_chosen_logps: Float[Tensor, "batch"],
    ref_rejected_logps: Float[Tensor, "batch"],
    beta: float = 0.1
) -> Float[Tensor, ""]:
    """
    DPO Loss: 优化策略以最大化 Chosen 和 Rejected 之间的隐含 Reward 差值。
    """
    # 1. 计算 Policy 和 Reference 的 Log 概率差 (Implicit Reward)
    # shape: (batch,)
    chosen_logratios = policy_chosen_logps - ref_chosen_logps
    rejected_logratios = policy_rejected_logps - ref_rejected_logps

    # 2. 计算 Logits (Reward 差值)
    logits = chosen_logratios - rejected_logratios

    # 3. 计算 Loss: -log(sigmoid(beta * logits))
    # 使用 logsigmoid 保证数值稳定性
    losses = -F.logsigmoid(beta * logits)

    return losses.mean()
```

**面试加分点**：
*   提到 `F.logsigmoid` 比 `torch.log(torch.sigmoid(...))` 数值更稳定。
*   清楚解释 `beta` 控制了对 Reference Model 的偏离程度（KL 惩罚系数的倒数）。

---

### 2. PPO Loss (Proximal Policy Optimization - Clip)

**核心点**：PPO 依赖 Advantage（优势函数），使用 Clip 机制限制更新步长，防止策略崩塌。这里只写核心的 **Policy Loss**。
**公式**：$L = \min(r_t A_t, \text{clip}(r_t, 1-\epsilon, 1+\epsilon) A_t)$

```python
def ppo_policy_loss(
    log_probs: Float[Tensor, "batch"],      # 当前策略产生的 log p
    old_log_probs: Float[Tensor, "batch"],  # 采样时旧策略的 log p
    advantages: Float[Tensor, "batch"],     # GAE 计算出的优势函数
    clip_eps: float = 0.2
) -> Float[Tensor, ""]:
    """
    PPO Clip Loss: 限制策略更新幅度。
    """
    # 1. 计算概率比率 r_t = exp(log_p - old_log_p)
    ratio = torch.exp(log_probs - old_log_probs)

    # 2. 计算未截断的 Loss 部分
    surr1 = ratio * advantages

    # 3. 计算截断后的 Loss 部分
    ratio_clipped = torch.clamp(ratio, 1.0 - clip_eps, 1.0 + clip_eps)
    surr2 = ratio_clipped * advantages

    # 4. 取最小值 (Pessimistic bound) 并取负号 (因为是梯度下降)
    loss = -torch.min(surr1, surr2)

    return loss.mean()
```

**面试加分点**：
*   强调 `advantages` 通常需要进行标准化（Normalize）以稳定训练。
*   解释为什么要取 `min`：这是为了形成一个悲观下界（Lower Bound），保证策略提升是安全的。

---

### 3. GRPO Loss (Group Relative Policy Optimization)

**核心点**：DeepSeek-V3/R1 使用的方法。**去掉了 Critic 模型**，通过对同一个 Prompt 采样一组（Group）输出来计算 Baseline。
**公式**：Advantage 通过组内标准化计算：$A_i = \frac{r_i - \text{mean}(R_{group})}{\text{std}(R_{group}) + \epsilon}$，然后套用 PPO 的 Clip Loss。

```python
def grpo_loss(
    log_probs: Float[Tensor, "b g"],      # b: batch(prompts), g: group_size
    old_log_probs: Float[Tensor, "b g"],
    rewards: Float[Tensor, "b g"],        # 每个采样的最终奖励
    clip_eps: float = 0.2,
    beta: float = 0.01                    # KL 惩罚系数 (可选)
) -> Float[Tensor, ""]:
    """
    GRPO: 无 Critic，使用组内归一化计算 Advantage。
    """
    # 1. 计算组内 Advantage (Group Relative)
    # 使用 einops 进行 reduce 操作，保持维度以便广播
    mean_rewards = reduce(rewards, "b g -> b 1", "mean")
    std_rewards = reduce(rewards, "b g -> b 1", "std")
    
    # 标准化 Advantage
    advantages = (rewards - mean_rewards) / (std_rewards + 1e-8)

    # 2. 计算 PPO Clip Loss (针对每个样本)
    ratio = torch.exp(log_probs - old_log_probs)
    surr1 = ratio * advantages
    surr2 = torch.clamp(ratio, 1.0 - clip_eps, 1.0 + clip_eps) * advantages
    
    ppo_loss = -torch.min(surr1, surr2) # shape: (b, g)

    # 3. (可选) 添加 KL 散度惩罚项 D_KL(pi || ref)
    # 近似计算: log_p - ref_log_p (这里简化假设 ref_log_p 已包含在输入或计算中)
    # ref_log_probs = ... 
    # kl_loss = torch.exp(ref_log_probs - log_probs) - ... (略)
    
    # 4. 聚合 Loss
    return ppo_loss.mean()
```

**面试加分点**：
*   **维度意识**：GRPO 的核心在于输入维度是 `(batch, group_size)`，而 PPO 通常是打平的 `(batch * seq_len)`。
*   **去 Critic**：明确指出 GRPO 节省了 Value Model 的显存和计算量，利用 `mean(rewards)` 作为 Baseline。
*   **Einops**：在这里使用 `reduce(..., "b g -> b 1", ...)` 非常优雅地展示了你对组内操作的理解。

---

### 总结复习 Cheat Sheet

| 算法 | 核心输入 | 核心机制 | 区别一句话 |
| :--- | :--- | :--- | :--- |
| **DPO** | Policy LogP, Ref LogP | Sigmoid(Implicit Reward Diff) | **无 RL 循环**，把 RL 问题转化为二分类 Loss。 |
| **PPO** | LogP, Old LogP, **Advantage** | Clip Ratio, Min(Surr1, Surr2) | **有 Critic**，通过 Value Model 计算 Advantage，限制更新步幅。 |
| **GRPO** | LogP, Old LogP, **Rewards(Group)** | **Group Norm**, PPO Clip | **无 Critic**，通过对同一问题多次采样计算相对优势。 |

面试时，建议先写出函数签名（输入输出维度），口头解释一下物理含义，然后再填充中间的计算逻辑。祝面试顺利！