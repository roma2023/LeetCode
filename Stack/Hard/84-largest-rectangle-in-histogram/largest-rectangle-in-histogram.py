class Solution:
    # Complexity Analysis:  
      
    # As we go through each height-idx pair once and push-pop once 
    # Time complexity = O(n)
    # As we registered all elements in stack once
    # Space Complexity = O(n)

    def largestRectangleArea(self, heights: List[int]) -> int:

        # holds maxArea
        maxArea = 0

        # stack of index, height tuples
        stack = []  # pair: (index, height)

        # for idx and height
        for i, h in enumerate(heights):

            # start idx
            start = i

            # while the stack isnt empty 
            # and top val height is greater than h
            while stack and stack[-1][1] > h:
                # we pop idx and height
                index, height = stack.pop()
                # check if this height is max area rectangle
                maxArea = max(maxArea, height * (i - index))
                # since the height > h, it means we can extend the h
                # so start = index
                start = index

            # now we push the start,h into stack
            stack.append((start, h))

        # some vals are still left
        for i, h in stack:
            # find area for each with len - i as all of them reached the end
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
