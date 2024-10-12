# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        
        if abs(leftHeight - rightHeight) > 1:
            return False
        
        # Recursively check if both left and right subtrees are balanced
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def getHeight(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        leftHeight = self.getHeight(node.left)
        rightHeight = self.getHeight(node.right)
        
        # Height of a node is 1 plus the height of the taller subtree
        return 1 + max(leftHeight, rightHeight)
