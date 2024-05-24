class Solution:
    # Complexity Analysis
    # As we go through each element once
    # Time Complexity = O(n)
    # As we save element in stack once
    # Space Complexity = O(n) 
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # initialize the res list with 0s
        res = [0] * len(temperatures)

        # make a stack 
        stack = []  # pair: [temp, index]

        # for index and value
        for i, t in enumerate(temperatures):
            # while the stack isnt empty and temperature is greater than
            # the temp of the last elemtn in stack

            while stack and t > stack[-1][0]:
                # pop the stack
                stackT, stackInd = stack.pop()
                # save the dif of indices at the lower index
                res[stackInd] = i - stackInd
            
            # append to stack
            stack.append((t, i))
        return res
