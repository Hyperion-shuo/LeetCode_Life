class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # answer one
        # length = len(nums)
        # temp = [0] * length
        # for i in  range(length):
        #     temp[(i + k) % length] = nums[i]
        # for i in  range(length):
        #     nums[i] = temp[i]

        # answer two
        # def swap(l, r):
        #     while (l <= r):
        #         nums[l], nums[r] = nums[r], nums[l]
        #         l+=1
        #         r-=1
        # n = len(nums)
        # k = k % n
        # swap(0, n - 1)
        # swap(0, k - 1)
        # swap(k , n - 1)

        # answer three
        n = len(nums)
        k = k % n
        count = 0
        start = 0
        while count < n:
            current_idx = start
            cuttent_num = nums[current_idx]
            while True:
                next_idx = (current_idx + k) % n
                next_num = nums[next_idx]
                nums[next_idx] = cuttent_num
                current_idx = next_idx
                cuttent_num = next_num
                count += 1
                if next_idx == start:
                    start += 1
                    break
