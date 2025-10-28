# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = root.val

        def findMax(root, res):
            if root == None:
                return (0, res)
        
            tl = findMax(root.left, res)
            left, res = tl[0], tl[1]
            tr = findMax(root.right, res)
            right, res = tr[0], tr[1]

            # parent-friendly path
            Max = max(left + root.val, right + root.val, root.val)

            # absolute path
            res = max(res, Max, left + root.val + right)
            return (Max, res)

        tup  = findMax(root, res)
        return tup[1]