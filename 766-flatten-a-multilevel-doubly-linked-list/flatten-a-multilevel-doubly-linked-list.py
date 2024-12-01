"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # edge case
        if not head: 
            return None

        # we can keep the next node before child node in the stack
        stack = []
        res = head

        # as long as one of the foloowing is not null
        while head.next or head.child or stack:

            # if 
            if not head.next and not head.child:

                parent, next = stack.pop()
                parent.next = parent.child
                parent.child.prev = parent
                parent.child = None

                if next: 
                    head.next = next
                    next.prev = head
                    head = next

            elif head.child:
               parent, next = head, head.next
               stack.append((parent, next))
               head = head.child 
            
            else: 
                head = head.next
        
        return res

            