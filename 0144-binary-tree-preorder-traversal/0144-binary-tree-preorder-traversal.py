# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        self.preOrderTravelsal(root,result)
        return result
    def preOrderTravelsal(self,node,result)->list[int]:
        if not node:
            return None
        result.append(node.val)
        self.preOrderTravelsal(node.left,result)
        self.preOrderTravelsal(node.right,result)



