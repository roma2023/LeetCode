# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # the tutrle and hopper alforithm 
        # we have turle and hopper
        if not head: return False
        turtle = head 
        hopper = turtle.next

        while hopper != turtle: 
            
            # makes two jumps
            if hopper and hopper.next and hopper.next.next:
                hopper = hopper.next.next
            else: return False

            #print(turtle.val, hopper.val)
            # makes 1 jump
            turtle = turtle.next

        return True
        