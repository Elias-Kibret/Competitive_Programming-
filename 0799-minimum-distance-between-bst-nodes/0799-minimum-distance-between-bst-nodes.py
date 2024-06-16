# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ls=[]

        def helper(node):
            if node is None:
                return
            helper(node.left)
            ls.append(node.val)
            helper(node.right)
        helper(root)
        ans=float("inf")

        for i in range(1,len(ls)):
            ans=min(ans,ls[i]-ls[i-1])

        return ans
        