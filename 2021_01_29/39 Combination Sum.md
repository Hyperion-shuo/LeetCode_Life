# 39. Combination Sum
[链接](https://leetcode-cn.com/problems/combination-sum/)

这道题的题意为，给定一个数组和数target，找出数组中所有加起来等于target的组合
组合可以选择重复的数。返回所有可能的组合，且返回的组合中不能重复

组合的问题可以使用回溯。
这道题的难点为，结果中不能重复。

列如target为5，则会出现（2，3） 和（3， 2）的组合，如果不在搜索时去重，而
在搜索完所有结果后再去重十分麻烦。这题应在搜索时去重。

去重的方法为每次搜索**限定下一次搜索的条件**，来保证结果不重复

解决方法为，搜索的时候限定每个分支能选择的元素
dfs(target, combine, idx)
如果包含idx则
dfs(target - candidates[idx], combine, idx)
否则跳过它
dfs(target, combine, idx + 1)

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)

        def dfs(target, combine, idx):
            if target <= 0:
                if target == 0:
                    result.append(combine.copy())
            else:
                combine.append(candidates[idx])
                dfs(target - candidates[idx], combine, idx)
                combine.pop()
                if idx < n - 1:
                    dfs(target, combine, idx + 1)

        dfs(target, [], 0)

        return result
```