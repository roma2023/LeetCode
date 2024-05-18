import functools
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pre = post = 1
        k = len(nums)

        for i in range(k-1):
            pre *= nums[i]  
            res[i+1] *= pre

            post *= nums[k-1-i]
            res[k-2-i] *= post
        
        return res

# O(n) time and space complexity, no use of division in the solution
