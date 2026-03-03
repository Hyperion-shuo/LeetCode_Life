# https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/description/

from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        num_sum = sum(nums)
        n = len(nums)
        num_k = int(num_sum // k)

        if n < k:
            return False
        
        if num_sum % k != 0:
            return False
        
        # 某些用例下去掉更快
        nums = sorted(nums)
        if num_k < nums[0]:
            return False

        used = [False] * n
        def dfs(idx, current_sum, k):
            if k == 0:
                return True

            if current_sum == num_k:
                return dfs(0, 0, k - 1)
            
            for i in range(idx, n):
                if used[i]:
                    continue

                if nums[i] + current_sum > num_k:
                    continue
                else:
                    used[i] = True
                    if dfs(i + 1, current_sum + nums[i], k):
                        return True
                    used[i] = False
                
                if current_sum == 0 and used[i] == False:
                    return False

                
        return dfs(0, 0, k)