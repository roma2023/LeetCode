class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # we know for sure that the array is rotated, amybe?
        # [l, ......, m, ......r] 
        # if l > r then the array is rotated 
            # l > m then we are on the right half of the rotation
                # target < m or target > l then go left
                # else: target > m and target < l, go right
            # else: l < m then we are on the right half of the rotation
                # target > l and target < m then go left
                # else: target > m or target < l then go right
        # else: array is sorted
            # ther is no disctinction here with above case they both will have it the same

        l, r = 0, len(nums) - 1

        while l <= r: 
            m = (r - l)//2 + l
            print(l,m,r)
            if target == nums[m]:
                return m

            if nums[l] > nums[m]:
                if target < nums[m] or target >= nums[l]:
                    r = m - 1
                else: 
                    l = m + 1
            else:
                if target < nums[m] and target >= nums[l]: 
                    r = m - 1
                else: 
                    l = m + 1
        print(l,m,r)
        return -1