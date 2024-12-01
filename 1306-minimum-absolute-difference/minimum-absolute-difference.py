class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # the BF approach O(n^2)
        # take every pair and calculate the diff and sort the result

        # sorting the list 
        # keep track of min difference between adjacent elements and we also want to 
        # record the pairs in a return array
        # TC => O(nlogn)

        res = []
        minDiff = float("inf") # or max(arr) - min(arr)
        sortedArray = sorted(arr)
        for i in range(len(arr) - 1): 
            Diff = sortedArray[i+1] - sortedArray[i]
            if minDiff > Diff: 
                minDiff = Diff
                res = [[sortedArray[i], sortedArray[i+1]]]
            elif minDiff == Diff:
                res.append([sortedArray[i], sortedArray[i+1]])
            
        return res

        # heap O(klogk)


        
            