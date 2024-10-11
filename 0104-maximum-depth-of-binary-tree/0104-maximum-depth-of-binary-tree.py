# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.maxDepthRec(root,0)
    def maxDepthRec(self, node: Optional[TreeNode],level) -> int:
        if not node:
            return -9223372036854775807
        if not node.left and not node.right:
            return level+1
        leftDepth=self.maxDepthRec(node.left,level+1)
        rightDepth=self.maxDepthRec(node.right,level+1)
        return max(leftDepth,rightDepth)
    
        