class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        # 单调栈
        mono_stack = []
        largest = 0
        # 存储左右第一个高度小于 heights[i] 元素的下标
        left_idx = [0] * n
        right_idx = [0] * n

        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            # -1 作为高度-inf的哨兵
            left_idx[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        mono_stack = []  # 清空
        for i in reversed(range(n)):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            # n 作为高度-inf的哨兵
            right_idx[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)

        for i in range(n):
            largest = max(heights[i] * (right_idx[i] - left_idx[i] - 1), largest)

        return largest

    # 简单方法， TL
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     n = len(heights)
    #     largest = 0
    #     for i in range(n):
    #         left = i
    #         right = i
    #         while right < n - 1 and heights[right+ 1] >= heights[i]:
    #             right += 1
    #         while left > 0 and heights[left - 1] >= heights[i]:
    #             left -= 1
    #         largest = max((right - left + 1) * heights[i], largest)
    #     return largest