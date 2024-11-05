class Solution:
    def jump(self, nums: List[int]) -> int:
        
        gap = 1
        minPath = [1000] * len(nums)
        minPath[len(nums) - 1] = 0
        numJumps = 0 

        # [2,3,1,1,0,4]
        for i in range(len(nums) - 2, -1, -1):
            
            if nums[i] >= gap:    
                             
                numJumps = 1 + min(minPath[i+1:] if i+1+nums[i] > len(nums) else minPath[i+1:i+1+nums[i]])
                minPath[i] = numJumps
                gap = 1
            else: 
                gap += 1
        return minPath[0]