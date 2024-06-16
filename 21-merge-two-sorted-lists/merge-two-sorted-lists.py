# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Complexity Aanalysis
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        merged = ListNode()
        root = merged

        while list1 and list2: 
            
            if list1.val < list2.val:
                merged.next = list1
                list1 = list1.next
                 
            else:
                merged.next = list2
                list2 = list2.next
                
            merged = merged.next
        
        if not list1: 
            merged.next = list2
        else:
            merged.next = list1
        return root.next
                
        