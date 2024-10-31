# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Base cases
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # Recursive case: compare the current nodes
        if list1.val <= list2.val:
            # list1's node is smaller, so include it in the result and move to the next node in list1
            newNode = ListNode(list1.val)
            newNode.next = self.mergeTwoLists(list1.next, list2)
        else:
            # list2's node is smaller, so include it in the result and move to the next node in list2
            newNode = ListNode(list2.val)
            newNode.next = self.mergeTwoLists(list1, list2.next)
        
        return newNode
