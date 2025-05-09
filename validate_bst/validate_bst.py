
# The idea is to know the range every time, you go left or right subtree
class Solution:
    def earsValidBST(self, root: Optional[TreeNode]) -> bool:

        def check_BST(root, min_val,max_val): 
            if root is None: 
                return True 

            if not ( min_val < root.val < max_val): 
                return False 
            
            return check_BST( root.left, min_val, root.val) and check_BST( root.right, root.val, max_val)
        
        return check_BST( root, float('-inf'), float('inf'))