# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True
#         return self.lenDiff(root,0)>=1
#     def lenDiff(self, node: Optional[TreeNode],level) -> int:
#         if not node:
#             return 0
#         if not node.left and not node.right:
#             return level+1
#         return abs(self.lenDiff(node.left,level+1)-self.lenDiff(node.right,level+1))
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkHeight(root) != -1

    def checkHeight(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0  # Base case: height of an empty tree is 0
        
        # Recursively check the height of left and right subtrees
        leftHeight = self.checkHeight(node.left)
        rightHeight = self.checkHeight(node.right)

        # If any subtree is unbalanced, propagate -1 upwards
        if leftHeight == -1 or rightHeight == -1:
            return -1

        # If the current node is unbalanced (height difference > 1), return -1
        if abs(leftHeight - rightHeight) > 1:
            return -1

        # Otherwise, return the height of the current subtree
        return max(leftHeight, rightHeight) + 1
