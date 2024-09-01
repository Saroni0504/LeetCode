'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
class Solution:
    def isValidBST(self, root):
        def is_valid(node,min_val,max_val):
            if not node: 
                return True
            if node.val <= min_val or node.val >= max_val:
                return False

            return is_valid(node.left,min_val,node.val) and is_valid(node.right,node.val,max_val)

        return is_valid(root,float('-inf'),float('inf'))
