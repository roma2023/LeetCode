# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        idx = 0
        start, end = ListNode(), ListNode()
        ptr = list1
        while ptr:
            if idx == a - 1: 
                start = ptr
            if idx == b + 1: 
                end = ptr
            idx += 1
            ptr = ptr.next

        start.next = list2
        while start: 
            last = start
            start = start.next
        last.next = end

        return list1
# TC => O(n + m) and SC => O(1)
