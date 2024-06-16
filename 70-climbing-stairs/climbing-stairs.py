class Solution:
    def climbStairs(self, n: int) -> int:
        # fibonacci series 
        """
        so at each step I either make 1 step or 2 steps, right?
        that means we can illustarate this with the decision tree

        0 -  1 - 2 - 3
        |.   |.  |
        2 -3 3   4
        |
        4
        O(2^n)
        cache them and use them again when needed

        0-1-2.     s(2) = s(1) + s(0). s(i) = s(i-1) + s(i-2)
        | 
        2

        ohh we have n staircases and we have this recurrence, 
        but how to use it ?
        
        we could do bottom-up approach, we know for sure that at 
        s(0) = 1
        s(1) = 1
        s(2) = s(1) + s(0).  0 ->  2steps - 2.     0-> 1step-> 1step-> 2
        s(3) = s(2) + s(1).    
        """ 
        one = 1
        two = 1

        for i in range(n-1): 
            temp = one
            one = one + two
            two = temp
        return one



