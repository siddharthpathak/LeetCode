# https://leetcode.com/problems/inorder-successor-in-bst/

# Successor of a node in a BST is the next nearest value which is greater than the node
# Using inorder traversal of a BST, we can easily get the next greater value but it would have a time complexity of O(n)
# Using the properties of BST, we can be sure of the following two things:
# 1. If the node has a right sub-tree then next closest greater value be the smallest value in the right sub-tree. 
# Because all the values are greater than the input node in the right sub tree, the one which will be nearest/closest to the current
# node would be the smallest one in the right sub tree.
# 2. If the node doesn't have a right sub-tree, then the next value greater than the current node would be a node in the parent chain.
# While traversing the tree we can keep track of the prev node encountered


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        # Initially we don't have any successor
        succ = None
        
        # Keep Traversing until we hit an end
        while root:
            # If the key node is greater than the current node we are sure the successor lies in the right sub-tree
            if p.val >= root.val:
                root = root.right
            # Else we have found a node which is greater than the key node i.e.a candidate for the successor
            else:
                succ = root
                root = root.left
        
        return succ
  
  
  
  
 # Recursive
 '''
 
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        prev_max = None
        
        return helper(root,prev_max,p.val)

def helper(root,prev_max,key):
    if root is None:
        return prev_max
    
    elif root.val <= key:
        return helper(root.right,prev_max,key)
    else:
        return helper(root.left,root,key)
 '''
