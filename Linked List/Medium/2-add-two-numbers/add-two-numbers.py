# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        deg = 0
        while l1: 
            num1 += 10**deg * l1.val
            l1 = l1.next
            deg += 1

        num2 = 0
        deg = 0
        while l2: 
            num2 += 10**deg * l2.val
            l2 = l2.next
            deg += 1

        res = num1 + num2
        print(num1, num2, res)
        digit = 0
        head = ListNode(0,None)
        ptr = head
        if res == 0: 
            return ListNode(0, None)
        while res: 
            digit = res % 10 # last digit
            res = res // 10

            new = ListNode(0, None)
            new.val = digit 
            head.next = new 
            head = head.next

        return ptr.next




        

         
            
