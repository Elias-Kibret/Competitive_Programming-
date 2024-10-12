# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1+self.countGood(root.left,root.val)+self.countGood(root.right,root.val)

    def countGood(self,root,val)-> int :
        if not root:
            return 0
        count=0
        if root.val>=val:
            val=root.val
            count=1
        return count +self.countGood(root.left,val)+self.countGood(root.right,val)
        