class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # we need to find powers for all ints in [lo, hi]
        # sort them based on power
        # return kth element 
        

        # brute force approach
        # find powers O(n * k(the average numebr of iterartions it takes to find the power of n )) => sort the list based on the powers => O(nlogn)
        # once we found the kth power, search for its host in the list

        # STEP 1: find powers
        def findPower(num: int) -> int:
            count = 0
            while num != 1:
                if num % 2: # odd
                    num = 3 * num + 1
                else: 
                    num = num // 2
                count += 1
            return count
        
        powers = [0] * (hi - lo + 1)
        for i in range(lo, hi + 1): 
            powers[i - lo] = (findPower(i), i)

        # STEP 2: sort them
        # print(powers)
        powers = sorted(powers, key = lambda tup: tup[0])
        # print(powers)
        return powers[k-1][1]


        
            
            