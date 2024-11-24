# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         def valid(node, left, right):
#             if not node:
#                 return True
#             if not (left < node.val < right):
#                 return False

#             return valid(node.left, left, node.val) and valid(
#                 node.right, node.val, right
#             )

#         return valid(root, float("-inf"), float("inf"))

class Solution:        
    def isValidBST(self, root: TreeNode) -> bool:
        res = []

        def inOrder(root):
            if not root: 
                return
            
            inOrder(root.left)
            res.append(root.val)
            inOrder(root.right)

            return
        inOrder(root)

        # now, check if the inOrder Travdersal is ordered
        for i in range(len(res) - 1):
            if res[i] >= res[i + 1]: 
                return False
        return True
            

