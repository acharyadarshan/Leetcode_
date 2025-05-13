# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # current = root 
        # while current: 
        #     if p.val > current.val and q.val > current.val: 
        #         current = current.right
        #     elif p.val < current.val and q.val < current.val: 
        #         current = current.left 
        #     else: 
        #         return current 

        #recurison solution 

# the idea is to explore left subtree first, and if you find say p then bubble up that value all the way to the top, that way left = p , then recurse on right, if you find q, then recurse that value all the way to top, that way you need split has occured and the root is where the split happened . If you find both p and q on one side, then whichever occours first happens to be the root, it's intuitive that if you find p first then q has to be descendant of the q and vice versa. 


        if not root or root == p or root == q: 
            return root
        
        left = self.lowestCommonAncestor( root.left, p, q )
        right = self.lowestCommonAncestor( root.right, p,q )

        if left and right: 
            return root 
        return left if left else right
