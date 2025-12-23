class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # step 1
        x, y = 0, 0
        for i in range(len(nums1)):
            if nums1[i] == 0:
                x += 1
        
        for i in range(len(nums2)):
            if nums2[i] == 0:
                y += 1


            # step 2
        sum1 = sum(nums1) + x
        sum2 = sum(nums2) + y
        
        # step 3
        if sum1 == sum2:
            return sum1
        
        # step 4
        if x > 0 and y > 0: 
                return max(sum1, sum2)
            
        # step 5
        elif x > y and sum1 < sum2:
            return sum2
        
        elif x < y and sum1 > sum2:
            return sum1
        
        else:
            return -1