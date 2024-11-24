# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = root.val
        
        def dfs(par): 
            if not par:
                return 0

            leftMax = dfs(par.left)
            rightMax = dfs(par.right)

            self.res = max(self.res, par.val,
                           par.val + leftMax, 
                           par.val + rightMax,
                    par.val + leftMax + rightMax)


            # return max of (parent alone, with leftMax, or with rightMax)
            return max(par.val, par.val + leftMax, par.val + rightMax)
        
        dfs(root)

        return self.res