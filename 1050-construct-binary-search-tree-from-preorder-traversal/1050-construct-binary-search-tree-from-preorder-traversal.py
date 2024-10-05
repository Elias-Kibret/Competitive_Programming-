# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        '''
        first we have to check if 
        the give preorder list is not 
        empty


        '''
        if not preorder:
            return None
        
        '''
        we need the root node to work 
        with it 

        '''
        root=TreeNode(preorder[0])

        def insertNodeBST(node:TreeNode, val:int)->[TreeNode]:
            '''
            this is when the root node left or right is null
            '''
            if not node:
                return TreeNode(val)
            if val< node.val:
                node.left=insertNodeBST(node.left,val)
            if val>node.val:
                node.right=insertNodeBST(node.right,val)
            return node
        for value in preorder[1:]:
            insertNodeBST(root,value)
        return root

            
