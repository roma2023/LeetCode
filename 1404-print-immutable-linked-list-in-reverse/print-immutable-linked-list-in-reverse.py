# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
       # curr_node-> null 
       # second_last -> last_node 
       # hashMap => value : freq
       # TC => O(n^2), SC => O(n) 

        if head == None:
            return
        
        # recursive solution
        def bt (head: 'ImmutableListNode') -> None:
            
            if head.getNext() == None:
                head.printValue()
                return

            bt(head.getNext())
            head.printValue()
            return
        
        bt(head)

        # input = [1,2,3,4] 
        # TC => O(n), SC => O(n) 

