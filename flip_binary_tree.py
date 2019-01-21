'''
Leetcode: https://leetcode.com/problems/flip-equivalent-binary-trees/

Approach #1: Traverse both the trees recursively and check if the left child is equal to the left or right child of the other tree

Approach #2: As we know that each number is going to be unique, then that number should have the same parent in both the trees. 
Traverse the first tree and store the node value and parent in an array. While traversing the second tree check if the parent is the same.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        
        return ((self.flipEquiv(root1.left,root2.left) and self.flipEquiv(root1.right,root2.right))
        or (self.flipEquiv(root1.left,root2.right) and self.flipEquiv(root1.right,root2.left)))
        
        
            
            
