class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Create a dummy node to simplify head swapping
        dummy = ListNode(0)
        dummy.next = head
        print(dummy.val)
        prev = dummy
      
       

        # Traverse the list in pairs
        while prev.next and prev.next.next:
            # Identify the two nodes to swap
            
            first = prev.next
           
            second = first.next

            # Swap the nodes
            prev.next = second          # Point prev to second
            first.next = second.next    # Point first to the node after the pair
            second.next = first         # Point second to first

            # Move prev to the end of the swapped pair
            prev = first

        # Return the new head of the list
        return dummy.next
