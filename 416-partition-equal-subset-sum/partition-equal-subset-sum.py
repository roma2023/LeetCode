class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2: return False
        
        dp = defaultdict(int) # totals 
        target = sum(nums) // 2
        dp[0] = 1
        for num in nums:
            for total in range(target, num-1, -1): 
                dp[total] = max(dp[total-num], dp[total])

        return dp[target]
        
        # def backtrack(i, total): 
        #     if total < 0: 
        #         return 0
        #     if i == len(nums): 
        #         return 1 if total == 0 else 0 
        #     if (i, total) in dp: 
        #         return dp[(i,total)]
            
        #     dp[(i, total)] = max(backtrack(i+1, total-nums[i]), 
        #                         backtrack(i+1, total))
        #     return dp[(i, total)]
        # return backtrack(0, target)