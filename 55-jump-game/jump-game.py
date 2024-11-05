class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gap = 1
        curr_idx = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            
            if nums[i] >= gap: 
                curr_idx = i 
                gap = 1
            else: 
                gap += 1
        
        return curr_idx == 0
            