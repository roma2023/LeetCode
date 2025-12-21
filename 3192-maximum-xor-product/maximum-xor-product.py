class Solution:

    
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
    # what do I know about XOR, I know that XOR it flips 1 when there are two different bits on both sites, and flips 0 when the both bits are the same 
    # 12 in binary form is 1100 => 11
    # 5 in binary form is 101 => 10
    # flip both 0100 => 4, 1101 => 13 => 
    
    # 1 in binary form is 001 => 110
    # 5 in binary form is 101 => 010
    # 6 in binary form is 110 => 001            
    # that means we need to construct a number so that it has bits 
    # in positons where both a and b don't
    # 
    # (a XOR x) * (b XOR x) => ab XOR ax XOR bx XOR x^2 => 
    # what if we add them first then do XOR => this is 6+1 then 
    # 
    # => ab XOR (a XOR b XOR x) * x
        
        if a < b:
            a, b = b, a

        x, a, b = self.buildX(a,b,n)
        print(x)
        ans = (a + x) * (b + x)
        return ans % (10**9 + 7)

    def buildX(self, a, b, n):
        copyA, copyB = a, b
        factor = 1
        ans = 0
        
        for i in range(n):
            aBit = copyA % 2
            bBit = copyB % 2

            if aBit == 0 and bBit == 0:
                ans += factor

            if aBit == 1 and bBit == 0:
                if a * b < (a - factor) * (b + factor):
                    a -= factor
                    b += factor

            factor *= 2
            copyA //= 2
            copyB //= 2

        return ans, a, b
