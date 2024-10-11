# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.minDepthRec(root, 0)

    def minDepthRec(self, node: Optional[TreeNode], level) -> int:
        
        if node == None:
            return 9223372036854775807
        if node.left == None and node.right == None:
            return level + 1

        left = self.minDepthRec(node.left, level+1)
        right = self.minDepthRec(node.right,level+1)
        
        return min(left,right)
    