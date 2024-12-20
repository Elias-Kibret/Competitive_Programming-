# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        currentSum=0

        return self.sumNodes(root,currentSum)

    
    def sumNodes(self,root,currentSum)->int:

        if not root:
            return 0
        currentSum=currentSum*10+root.val

        if not root.left and not root.right:
            return currentSum
        leftSum=self.sumNodes(root.left,currentSum)
        rightSum=self.sumNodes(root.right,currentSum)
        return leftSum+rightSum

        