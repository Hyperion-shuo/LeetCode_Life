import collections
from typing import List

# class Solution:
#     def findMaxLength(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n <= 1:
#             return 0
        
#         cum_sum = [0] * n
#         cum_sum[0] = 1 if nums[0] == 1 else -1
#         d = {}
        
#         if cum_sum[0] not in d:
#             d[cum_sum[0]] = 0
        
#         for i in range(1, n):
#             change = 1 if nums[i] == 1 else -1
#             k = cum_sum[i - 1] + change
#             cum_sum[i] = k
#             if k not in d:
#                 d[k] = i
            
#         max_len = 0
#         d[0] = -1
#         for i in range(n):
#             k = cum_sum[i]
#             if k in d:
#                 max_len = max(max_len, i - d[k])
                
#         return max_len

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 哈希表初始化：前缀和为0出现在下标-1
        hash_map = {0: -1}
        
        max_len = 0
        current_sum = 0
        
        for i, num in enumerate(nums):
            # 1. 更新前缀和
            if num == 1:
                current_sum += 1
            else:
                current_sum -= 1
            
            # 2. 检查并计算
            if current_sum in hash_map:
                # 如果这个和出现过，说明中间这段的和为0
                # 长度 = 当前下标 - 第一次出现的下标
                max_len = max(max_len, i - hash_map[current_sum])
            else:
                # 3. 如果没出现过，记录下来（只记录第一次，保证最长）
                hash_map[current_sum] = i
                
        return max_len
    
s = Solution()
r = s.findMaxLength([0,1,1,1,1,1,0,0,0])