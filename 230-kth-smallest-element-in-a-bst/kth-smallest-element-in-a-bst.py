# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root
        last = 0
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            # stackP = [e.val for e in stack]
            # print(stackP)
            curr = stack.pop()
            
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

            

                
        
