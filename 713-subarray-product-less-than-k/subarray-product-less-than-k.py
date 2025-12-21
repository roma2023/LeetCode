class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # off top of my head, if I think of the most obvious solution that would
        # be taking all possible contigious subarray so of this array
        # like by [10, 5, 2, 6] => O(n^2), O(n) just calculate product of subarray
        # overall costing us O(n^3) solve this problem
        # smarter brute force approach would be a sliding window 
        # [10, 2, 2, 4, 6] O(n^2)
        # we can do better, we need a real sliding window, if the subarray of 4 elements satisfy our condition then all possible subsets of such subarray ca also satisfy our condition, hence we dont have recalculate that
        # [1,2,3,4,5],
        if k <= 1: 
            return 0

        ans = 0
        subProduct = 1
        i, j = 0, 0
        while i <= j and i < len(nums) and j < len(nums):
            while j < len(nums) and nums[j] >= k:
                
                subProduct = 1
                i, j = j+1, j+1

            if j < len(nums) and subProduct < k:
                
                
                subProduct *= nums[j]
                
                if subProduct < k:
                    print(j-i+1)
                    ans += (j-i+1)
                    j += 1
                else:
                    while subProduct >= k and i<=j:
                        subProduct /= nums[i]
                        i += 1  
                    subProduct /= nums[j]
        return ans
        