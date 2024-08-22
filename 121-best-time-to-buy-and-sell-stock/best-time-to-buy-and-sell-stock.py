class Solution:
    # Complexity Analysis
    # TC = O(n) and SC = O(n) 
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        minP = max(prices)
        maxP = 0

        for price in prices: 
            if price < minP: 
                maxProfit = max(maxProfit, maxP - minP)
                minP = price
                maxP = price
            else: 
                maxP = max(maxP, price)
            print(minP, maxP)
        return max(maxProfit, maxP - minP)
