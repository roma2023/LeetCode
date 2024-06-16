# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        temp = None

        ptr = head
        head = head.next
        ptr.next = None

        while head: 
            
            temp = ptr
            ptr = head
            head = head.next
            ptr.next = temp
        
        return ptr
