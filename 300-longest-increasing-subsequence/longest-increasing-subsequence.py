class Solution:
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     LIS = [1] * len(nums)

    #     for i in range(len(nums) - 1, -1, -1):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] < nums[j]:
    #                 LIS[i] = max(LIS[i], 1 + LIS[j])
    #     return max(LIS)

    def lengthOfLIS(self, nums):
        # [1,2,4,3] -> [2,4,3] -> [4,3] -> [3] => 
        # dp[3] => 1, 
        # dp[2] => for i in range(next) => if dp[i] > dp[2]: dp[i] = max(dp[2], 1 + dp[i])

        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]: 
                     dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
