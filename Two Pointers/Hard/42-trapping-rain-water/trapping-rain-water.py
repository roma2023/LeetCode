class Solution:
    def trap(self, height: List[int]) -> int:

        """
        the solution here is very visible, we can use two pointers one on the left and another on the right, then find the left and right bounds as we move the pointers, and the difference of the lower heights from those bounds are gonna be the blocks of water we trap 

        let's see it on the example of sample input: 
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 2, 1]

        at first left = 0, right = 1
        we see the left_bound is 0, but right_bound = 1, so we cant trap any water in-between as it would spilt out towards left right

        then we can move left = 1 because its the limiting factor
        now, left_bound = 1 and right_bound = 1, now we can trap some water inside these bounds

        now as move left = 0 and right = 2
        we see that left_bound = 1 and right_bound = 2 
        this left is now less than the min(left_bound, right_bound)
        
        hence trapped_water += min(l_bound, r_bound) - left

        and we see that left_bound is again a limiting factor, and we move it 
        left = 2 and left_bound = 2 same as right_bound

        we move both left = 1 and right = 1, they both can be filled 1 block of water
        and so on, I believe this became clear now
        and we can code it up, before that let's analyze the complexity, this is gonnatake linear time O(n) because go through the n size list only once
        """
        left, right = 0, len(height) - 1
        left_bound = 0
        right_bound = 0
        trapped_water = 0

        while left < right:
            left_bound = max(left_bound, height[left])
            right_bound = max(right_bound, height[right])

            if  left_bound < right_bound:
                trapped_water += left_bound - height[left]
                left += 1 
            else: 
                trapped_water += right_bound - height[right]
                right -= 1

        return trapped_water 

