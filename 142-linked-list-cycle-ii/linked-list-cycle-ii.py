# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ok, we know the size of the ll => n 
        # also we know how much turtle will travel, let it be t
        # we also know how much hare will travle, let it be h
        # if t == h, then this is ex: n = 4, t = 3, h = 3*2 

        Set = set()
        slow = head
        while slow:
            if slow in Set: 
                return slow
            Set.add(slow)
            slow = slow.next

        

        