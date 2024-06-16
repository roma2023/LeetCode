class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        parentIdx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : parentIdx + 1], inorder[:parentIdx])
        root.right = self.buildTree(preorder[parentIdx + 1 :], inorder[parentIdx + 1 :])
        return root
