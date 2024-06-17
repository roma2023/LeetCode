class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r: 
            # if sorted
            if nums[l] < nums[r]: 
                res = min(res, nums[l])
                break

            # if not sorted
            mid = (r-l)//2 + l
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]: 
                l = mid + 1
            else: 
                r = mid - 1
        return res