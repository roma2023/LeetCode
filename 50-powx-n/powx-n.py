# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         # brute force => just multiply by n in a loop of O(n)
#         # optimized => divide and conquer, logn 
#         if x == 0:
#             return 0 

#         # logn for space because of reccurrence stack
#         def rec(x, n):
#             if n == 0:
#                 return 1
#             if x == 0:
#                 return 0 

#             # go to the depth till we reach n == 0, then build up the res back
#             res = rec(x, n // 2)
#             res = res * res

#             return x * res if n%2 else res
        
#         res = rec(x, abs(n))
#         return res if n>=0 else 1/res # if n is positive then res if negative 1/res


class Solution:
    def binaryExp(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        # Perform Binary Exponentiation.
        result = 1
        while n != 0:
            # If 'n' is odd we multiply result with 'x' and reduce 'n' by '1'.
            if n % 2 == 1:
                result *= x
                n -= 1
            # We square 'x' and reduce 'n' by half, x^n => (x^2)^(n/2).
            x *= x
            n //= 2
        return result

    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        res = self.binaryExp(x, abs(n))
        if n >= 0:
            return res
        return 1/res