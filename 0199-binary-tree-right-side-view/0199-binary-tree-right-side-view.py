# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.rightView(root, result, 0)
        return result

    def rightView(self, node: Optional[TreeNode], result: List[int], level: int) -> None:
        # print(result)
        if not node:
            return
        
        # If this is the first time we've visited this level, add the node's value
        if level == len(result):
            result.append(node.val)
        
        # Traverse the right side first
        self.rightView(node.right, result, level + 1)
        print(level)
        # Then traverse the left side
        self.rightView(node.left, result, level +1)
        print(level)
