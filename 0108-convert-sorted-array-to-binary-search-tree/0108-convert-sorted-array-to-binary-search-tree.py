# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        '''
        Find the middle of the nums
        the call recusively 
        
        '''
        md=len(nums)//2
        root = TreeNode(nums[md])
        root.left=self.sortedArrayToBST(nums[:md])
        root.right=self.sortedArrayToBST(nums[md+1:])
        return root
       