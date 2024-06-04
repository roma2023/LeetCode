class Solution:
    # TC = O (logn)
    # just utilize FindMin algo and BS
    # return both the min and index of it in FindMin
    # Use it to make proper sorted nums and apply BS
    # consider the idx of min when returning the target idx

    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        res = (10000, 0)

        while l <= r:
            m = l + ((r - l) // 2)

            # if l > r, this means the list is rotated
            # if res > nums[l] the prev m val is greater than nums[l]
            if nums[l] <= nums[r]:
                return min(res, (nums[l], l))

            # if the left > right val
            # and mid greater than right, move l to mid
            elif nums[m] > nums[r]:
                l = m + 1

            # if mid less than right, save mid and move r to mid
            else:
                res = (nums[m],m)
                r = m - 1

    def search(self, nums: List[int], target: int) -> int:

        Min, Start = self.findMin(nums)
        #print(Min, Start)
        

        l, r = 0, len(nums) - 1
        nums = nums[Start:] + nums[0:Start]
        #print(nums)

        while l <= r:
            m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return (m + Start) % len(nums)
        return -1
