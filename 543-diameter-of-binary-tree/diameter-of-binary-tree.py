# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    Max = 0 
    def R (self, root, l, r): 
        if not root: return -1

        r = self.R(root.right, l, r) + 1
        l = self.R(root.left, l, r) + 1

        if self.Max < l + r:
            self.Max = l + r  

        return max(l,r) 


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.R (root, 0, 0)
        return self.Max