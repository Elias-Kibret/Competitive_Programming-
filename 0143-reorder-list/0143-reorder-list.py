# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorders the linked list in-place to alternate between the first and last nodes.
        """
        if not head or not head.next or not head.next.next:
            return  # Edge cases: empty list, single node, or two nodes

        # Find the middle of the linked list
        middle = self.findMiddle(head)
        
        # Split the list into two halves
        second_half = middle.next
        middle.next = None  # Break the connection
        
        # Reverse the second half
        reversed_middle = self.reverseLinkedList(second_half)
        
        # Merge the two halves
        first_half = head
        while first_half and reversed_middle:
            temp1 = first_half.next
            temp2 = reversed_middle.next

            # Interleave nodes
            first_half.next = reversed_middle
            reversed_middle.next = temp1

            # Move to the next nodes
            first_half = temp1
            reversed_middle = temp2

    def findMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Finds the middle node of the linked list using the slow and fast pointer approach.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses the linked list starting from the given head node.
        """
        prev, current = None, head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
