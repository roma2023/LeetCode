class Solution:
    def rob(self, nums: List[int]) -> int:

        # ok, let's solve the sub problem which is max amount of money we can rob from 1 house nghbh
        # [1,2,3,1]
        # [1] => max = 1, [3,1] => max(3,1), 
        # [2,3,1] => you either take 2 + dp[0] or dp[1]
        # rob1 = 0, rob2 = 0
        # rob1, rob2 = 1 + 0, 0
        # rob1, rob2 = 3 + 0, 1


        maxRob = 0
        rob1, rob2 = 0, 0  

        for i in range(len(nums) - 1, -1, -1):

            rob1, rob2 = max((nums[i] + rob2), rob1), rob1

        return max(rob1, rob2)