class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # m * m-1 => O(m^2).    O(1)
        # start = [s1,s2,s3 ... ] O(mlogm)
        # greedy, minStart => iterate each s, s < minStart
        # minEnd => e > minEnd 
        # secondMin, firstMin
        # secondMax, firstMax

        

        firstMin, firstMax =  (arrays[0][0], 0), (arrays[0][-1], 0)
        secondMin, secondMax = (arrays[1][0], 1), (arrays[1][-1], 1)

        for i in range(len(arrays)):
            s, e  = arrays[i][0], arrays[i][-1]
            if firstMin[0] > s: 
                secondMin = firstMin
                firstMin = (s, i)
        
            elif secondMin[0] > s and i != firstMin[1]: 
                secondMin = (s,i)
                
            if firstMax[0] < e: 
                secondMax = firstMax
                firstMax = (e, i)
            
            elif secondMax[0] < e and i != firstMax[1]: 
                secondMax = (e, i)
        
        print(firstMin, firstMax, secondMin, secondMax)
        if firstMin[1] != firstMax[1]:
            return abs(firstMax[0] - firstMin[0])
        else: 
            return max(abs(firstMax[0] - secondMin[0]), abs(secondMax[0] - firstMin[0]))

            