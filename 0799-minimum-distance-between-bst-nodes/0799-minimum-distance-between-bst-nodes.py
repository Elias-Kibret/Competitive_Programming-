# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # ls=[]

        # def helper(node):
        #     if not node:
        #         return []
        #     return helper(node.left)+[node.val]+helper(node.right)
          
        # ls=helper(root)
        # ans=float("inf")

        # for i in range(1,len(ls)):
        #     ans=min(ans,ls[i]-ls[i-1])

        # return ans
        

        prev=-float('inf')
        min_diff=float('inf')


        def in_order(node):
            nonlocal prev,min_diff
            if not node:
                return
            in_order(node.left)
            min_diff=min(min_diff,node.val-prev)
            prev=node.val
            in_order(node.right)
        in_order(root)
        return min_diff