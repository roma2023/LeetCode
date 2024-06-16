# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge2List(self, first: ListNode, second: ListNode) -> ListNode: 
        
        head = ListNode() 
        root = head
        print(first, second)
        while first and second: 
            print(first.val, second.val)
            if first.val < second.val: 
                 
                head.next = first
                first = first.next
            else: 
                head.next = second
                second = second.next
                
            head = head.next

        if not first: 
            head.next = second 
        else: 
            head.next = first 
        
        return root.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        
        # do merge sort
        while len(lists) > 1:
            newList = []
            for i in range(0, len(lists), 2): 
                first = lists[i] 
                second = lists[i+1] if i + 1 < len(lists) else None 
                newList.append(self.merge2List(first, second))
            lists = newList 
        
        return lists[0] 
    

                           