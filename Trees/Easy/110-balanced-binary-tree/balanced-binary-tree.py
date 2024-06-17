# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self): 
        self.balanced = True
    def depth(self, root, l, r): 
        if not root: 
            return 0
        l = self.depth(root.left, l, r) + 1
        r = self.depth( root.right, l, r) + 1

        if abs(l-r) > 1: 
            self.balanced = False
        return max(l,r)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        depth = self.depth(root, 0, 0)
        return self.balanced