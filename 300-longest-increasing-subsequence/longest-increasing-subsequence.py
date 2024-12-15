class Solution:
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     LIS = [1] * len(nums)

    #     for i in range(len(nums) - 1, -1, -1):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] < nums[j]:
    #                 LIS[i] = max(LIS[i], 1 + LIS[j])
    #     return max(LIS)

    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size

    # Runtime: 48 ms