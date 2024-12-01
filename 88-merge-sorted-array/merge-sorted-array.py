class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        '''
        Time complexity: O(m+n)
        Space complexity: O(1)
        '''
        
        midx = m - 1 # this is for the 
        nidx = n - 1 
        right = m + n - 1

        while nidx >= 0:
            if midx >= 0 and nums1[midx] > nums2[nidx]:
                nums1[right] = nums1[midx]
                midx -= 1
            else:
                nums1[right] = nums2[nidx]
                nidx -= 1

            right -= 1