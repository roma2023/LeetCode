class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(n)/O(1) : Time/Memory
        
        res = max(nums)
        maxP, minP  = 1, 1

        for n in nums: 
            if n == 0: 
                maxP, minP = 1, 1
                continue
            
            tmp = max(maxP * n, minP * n, n)
            minP = min(maxP * n, minP * n, n)
            maxP = tmp

            res = max(res, maxP)
        return res
