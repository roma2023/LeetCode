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

        # Set = set()
        # slow = head
        # while slow:
        #     if slow in Set: 
        #         return slow
        #     Set.add(slow)
        #     slow = slow.next
        # # TC => O(n) and Sc => O(n)

        
        # Initialize two pointers, slow and fast, to the head of the linked list.
        slow = head
        fast = head

        # Move the slow pointer one step and the fast pointer two steps at a time through the linked list,
        # until they either meet or the fast pointer reaches the end of the list.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # If the pointers meet, there is a cycle in the linked list.
                # Reset the slow pointer to the head of the linked list, and move both pointers one step at a time
                # until they meet again. The node where they meet is the starting point of the cycle.
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        # If the fast pointer reaches the end of the list without meeting the slow pointer,
        # there is no cycle in the linked list. Return None.
        return None
        


        


        

        