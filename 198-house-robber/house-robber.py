class Solution:
    def rob(self, nums: List[int]) -> int:

        # ok, let's solve the sub problem which is max amount of money we can rob from 1 house nghbh
        # [1,2,3,1]
        # [1] => max = 1, [3,1] => max(3,1), 
        # [2,3,1] => you either take 2 + dp[0] or dp[1]

        dp = [0] * (len(nums) + 2) 

        for i in range(len(nums) - 1, -1, -1): 
            dp[i] = max(dp[i + 2] + nums[i], dp[i+1])

        return max(dp)