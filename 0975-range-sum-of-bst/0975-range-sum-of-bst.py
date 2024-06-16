# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total=0

        if root==None:
            return 0
        if root.val>=low and root.val<=high:
            total+=root.val
        return total+self.rangeSumBST(root.left,low,high)+self.rangeSumBST(root.right,low,high)

        
        