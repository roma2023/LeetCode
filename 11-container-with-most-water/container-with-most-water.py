class Solution:
    def calculate_area(self, left: int, right: int, height: List[int]) -> int: 
            area = (right-left) * min(height[left], height[right])
            return area
    
    def maxArea(self, height: List[int]) -> int:

        """
        just to clarify what's the range of heights we can take in? Can it be 0? 
        can the list be  empty?

        hmmm ok, alright let me think about this

        visually looking we need to find the two bounds of the container and we can observe that it would take the height of the min value between them, then it would suffice to multiply the diffrence of indices by that minimum height to find the area water can fill in right

        for example, [1,8,5,6,9] => the area between peaks 8 and 5 would be (2-1) * min(5,8) = 1*5 = 5

        so, the brute force solution that comes to my mind, is just permute over all possible pairs of peaks and keep using the above operation to find the max area we can get

        however, this is very costly, as a matter of fact this would be O(n^2) time complexity ufffff. 

        Then, how could we do better? lemme think, I think as we go through the list we can notice that it would suffice to just keep track of the maximum area as we shrink left and right pointers

        so for [1,8,5,6,9] we keep track of leftmost and rightmost pointers because at first we wanna maximize the length right, then we can shrink the bounds in order to maximize the heights, if the left height is greater than right height we shrink right pointer, else we shrink right pointer. as we would do consatnt work as we go over the whole list once the overall complexity would be O(n), so that's great

        """
        left, right = 0, len(height) - 1
        max_area, areaLR = 0, 0

        while left < right:
            
            area = self.calculate_area(left, right, height)
            max_area = max(max_area, area)
            
            if height[left] > height[right]:
                right -= 1
            else: 
                left += 1

        return max_area 








