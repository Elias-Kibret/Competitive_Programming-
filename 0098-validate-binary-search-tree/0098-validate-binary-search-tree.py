# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result=[]
        self.inorderBST(root,result)
        temp=result[:]
        temp=list(set(result))
        temp.sort()
        return temp==result
    def inorderBST(self, node,result)->list[int]:
        if not node:
            return None
        self.inorderBST(node.left,result)
        result.append(node.val)
        self.inorderBST(node.right,result)


        