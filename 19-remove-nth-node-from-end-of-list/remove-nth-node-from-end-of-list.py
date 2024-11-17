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

        #     1 -> 2 -> 3 -> 4 -> 5 -> null.    n = 2
        #     right = head, after 2 moves right = 3
        #     we deploy left = 1, then move both till right.next = null, then do left.next = right, then return root
        
        dummy = ListNode(0, head)
        right = head
        while n != 0 and right: 
            right = right.next
            n -= 1

        left = dummy
        while right: 
            right = right.next
            left = left.next

        print(left, right)
        left.next = left.next.next
        
        return dummy.next

        


        