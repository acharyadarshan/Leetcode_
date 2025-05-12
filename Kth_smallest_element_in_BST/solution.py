class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0

        def inorder(node):
            if node is None:
                return None

            # Try left
            left = inorder(node.left)
            if left is not None:
                return left

            # Visit this node
            self.count += 1
            if self.count == k:
                return node.val

            # Try right
            return inorder(node.right)

        return inorder(root)
