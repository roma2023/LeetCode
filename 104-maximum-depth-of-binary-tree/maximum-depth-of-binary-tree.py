# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root: 
    #         return 0
    #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# if they want iterative solution we have two solutions BFS(q) and DFS(stack):

    # # BFS => queue
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0

    #     q = collections.deque([root])
    #     depth = 0

    #     while q:
    #         for i in range(len(q)):
    #             node = q.popleft()
    #             if node.left: 
    #                 q.append(node.left)
    #             if node.right:
    #                 q.append(node.right)
        
    #         depth += 1

    #     return depth

    # DFS => stack
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        
        stack = collections.deque([[root, 1]])
        res = 0

        while stack:
            node, depth = stack.pop()
            
            if node:
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
                res = max(res, depth)
        return res

