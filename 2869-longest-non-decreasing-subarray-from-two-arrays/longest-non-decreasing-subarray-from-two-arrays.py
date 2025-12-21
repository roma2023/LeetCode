class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:

        if len(nums1) == 1:
                return 1
        
        ans = 1
        dp1, dp2 = 1, 1
        
        for i in range(len(nums1) - 2, -1, -1):
            # case 1: num1 val is less than num1 prev val
            temp1 = 1
            if nums1[i] <= nums1[i + 1]:
                temp1 = dp1 + 1			
            # case 2: num1 val is less than num2 prev val
            if nums1[i] <= nums2[i + 1]:
                temp1 = max(temp1, dp2 + 1)
        
            # case 3: num2 val is less than num1 prev val
            temp2 = 1
            if nums2[i] <= nums1[i + 1]:
                temp2 = dp1 + 1			
            # case 4: num2 val is less than num2 prev val
            if nums2[i] <= nums2[i + 1]:
                temp2 = max(temp2, dp2 + 1)
            
            dp1, dp2 = temp1, temp2
            ans = max(temp1, temp2, ans)
            
        return ans