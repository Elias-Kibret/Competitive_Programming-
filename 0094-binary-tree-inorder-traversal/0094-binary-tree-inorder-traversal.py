# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls=[]
        self.inOrder(root,ls)
        print(ls)
        return ls
    def inOrder(self,root,ls)->None:
        if not root:
            return None
  
        self.inOrder(root.left,ls)
        ls.append(root.val)
        self.inOrder(root.right,ls)
        