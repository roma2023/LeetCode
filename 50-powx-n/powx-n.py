class Solution:
    def myPow(self, x: float, n: int) -> float:
        # brute force => just multiply by n in a loop of O(n)
        # optimized => divide and conquer, logn 
        if x == 0:
            return 0 

        def rec(x, n):
            if n == 0:
                return 1
            if x == 0:
                return 0 

            res = rec(x, n // 2)
            res = res * res
            return x * res if n%2 else res
        
        res = rec(x, abs(n))
        return res if n>=0 else 1/res

            