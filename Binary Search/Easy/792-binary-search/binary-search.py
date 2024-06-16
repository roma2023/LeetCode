class Solution:
    # TC = O(logn)
    # SC = O(n)
    def search(self, nums: List[int], target: int) -> int:
        # use binary search
        # revision
        # ex: [-1,0,3,5,9,12] l,m,r = 0,2,5
        # if m < target : if m < 9 then l = m+1 and r no changed 
        # m = (r-l)//2 + l
        # if m > target: if m > 9 then l no changed and r = m

        l,r = 0, len(nums) - 1

        while l <= r:
            
            m = (r-l)//2 + l
            #print(l,m,r)

            if nums[m] < target:
                #print("case 1")
                l = m+1
            elif nums[m] > target:
                #print("case 2")
                r = m-1
            else:
                return m
        return -1
        
        