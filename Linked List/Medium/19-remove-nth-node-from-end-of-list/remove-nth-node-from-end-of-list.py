# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # TC = O(n)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #just make a ptr to before nth node 
        # as we move along the linked list, 
        # we will also be moving our before ptr
        # then make before point to the next next node skipping nth
        before = ListNode(0, head)
        root = before
        counter = 0
        while head:
            head = head.next
            counter += 1
            if counter >= n+1:
                before = before.next

        before.next = before.next.next
        return root.next
        


        