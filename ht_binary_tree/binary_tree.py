
class TreeNode: 
    def __init__( self, val, left, right): 
        self.val = val
        self.left = left
        self.right = right 

    def max_height(self, root):
        if root is None: 
            return 0 
        left = self.max_height(root.left)
        right = self.max_height(root.right)
        return max(left, right) + 1
    
    def tree_sum(self, root): # to return the total sum of values
        if root is None: 
            return 0 
        left = self.tree_sum(left.sum)
        right = self.tree_sum(right.sum)
        return root.data + left + right # to return max sum of left or right , just do max(left, right) + root

# finding one or more bases cases, calling recursion on left, and then right, and then joining the results
        # finding max value ( which node has max value basically)
        # if root is None, return float(-inf), max(root.data, left, right)

# checking if specific value exists in the tree, 
    
    def exists_in_Tree(self, root, value): 
        if root is None: 
            return False
        else: 
            check_left = self.exists_in_Tree(root.left, value)
            check_right = self.exists_in_Tree(root.right, value)
            return root.data == value or check_left or check_right
# reverse a binary tree
    
    def reverse_tree(self,root): 
        if root is None: 
            return 
        else: 
            self.reverse_tree(root.left)
            self.reverse_tree(root.right)
            root.left, root.right = root.right, root.left