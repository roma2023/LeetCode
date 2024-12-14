class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # here we can simply find sum of possible decrements per each index
        # for example, queries [[1,3],[0,2]] mean that we can decrement 
        # index 0 once, index 1,2 twice max, and index 3 once again
        # once, we find such number of possible decrements for each index
        # we can simply check each number's value vs the max decrements
        # if num > dec then we cant turn it 0, right
        # Also, its important to take care ofa case when num is negative, as we can only
        # decrement we cannot have negative vals

        
        # lets make a hashmap, or justa. simple list of tuples iof form (inc, dec)
        
        decs = [[0,0] for i in range(len(nums) + 2)]
        for q in queries:
            decs[q[0]][0] += 1
            decs[q[1] + 1][1] += 1
        
        print(decs)

        incVal = 0
        for i in range(len(nums)):
            incVal += decs[i][0] - decs[i][1]
            print(incVal)
            if nums[i] > incVal:
                return False
        
        return True