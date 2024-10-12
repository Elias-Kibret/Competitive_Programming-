# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        result=[]
        self.inorderTraversal(root,result)
        # if len(result)>=2:
        #     return result[1]
        temp=[]
        check=set()
        for val in result:
            if val not in check and val!=None:
                temp.append(val)
                check.add(val)
        print(temp)
        temp.sort()
        if len(temp)>1:
            return temp[1]
        return -1
    def inorderTraversal(self,root,result)->list[int]:
        if not root:
            return None
        self.inorderTraversal(root.left,result)
        result.append(root.val)
        self.inorderTraversal(root.right,result)
    
        