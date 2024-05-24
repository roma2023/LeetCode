class Solution:
    # Complexity Analysis
    # As we are goiung through the pos, speed pair once each its O(n), 
    # but we also use the sort function,so 
    # Time Complexity = O(nlogn)
    # we have the array of n elements, and we also save them in stack
    # Space Complexity = O(n)
    
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # so the idea here is that if there is a car that is far behind
        # yet it can reach the target faster or same time as you
        # that means you nust collide at some point

        # make the pos, speed tuple list
        pair = [(p, s) for p, s in zip(position, speed)]

        # reverse sort it, so the higher poss are first
        pair.sort(reverse=True)
        #print("pair: ", pair)
        stack = []

        for p, s in pair:  # Reverse Sorted Order
            #print("p,s: ", p,s)
            
            # save the number of hours it takes to reach the target
            stack.append((target - p) / s)
            
            #print("append stack: ", stack)
            # if the last car takes faster than the previous car pop it out
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                
                #print("last popped")
                stack.pop()

        return len(stack)
