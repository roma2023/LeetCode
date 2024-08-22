class Solution:
    def findComplement(self, num: int) -> int:
        # all we need to do is to find the number of bits needed to 
        # represent the number, then take the largest such number and 
        # return its difference from the given number
        # Example: 5 can be represented as 101, so 3 bits needed
        # the largest enumber that can be represent with 3 bits is 7 => 111
        # the complement of 5 is 7 - 5 => 2 

        # Subproblem=> find the number of bits needed to represent a number
        # we know 2^i => gives the num of nums that can be represented by i bits
        # where 2^i - 1 is the largest such number 
        # i = ceil(lg(n)) 

        i = math.floor(math.log(num, 2)) + 1
        maxNum = (2**(i)) - 1
        print(i, maxNum)
        return maxNum - num

        
        