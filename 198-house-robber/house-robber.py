class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = nums + [0]
        # [1,2,3,1] => [1,2,3,1,0]
        for i in range(len(dp) - 3, -1, -1): 
            dp[i] = max(dp[i+1], dp[i] + dp[i+2])
        return dp[0]