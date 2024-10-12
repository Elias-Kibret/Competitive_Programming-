# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        self.preorderTraverse(root, result)
        print(result)  # For debugging, can be removed later
        return result

    def preorderTraverse(self, node: 'Node', result: List[int]) -> None:
        if not node:
            return
        result.append(node.val)
        if node.children:  # Check if there are children
            for child in node.children:
                self.preorderTraverse(child, result)
