class Solution:
    # Complexity Analysis
    # TC = O(n) and SC = O(n) 
    def maxProfit(self, prices: List[int]) -> int:
        
        Min = 10000
        dif = 0

        for p in prices:
            if p < Min: 
                Min = p
            dif = max(dif, p - Min)
            #print(Min,Max, dif)
        return dif