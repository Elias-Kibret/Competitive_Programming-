# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        while head and head.val==val:
            head=head.next
        temp=head
        while temp:
            if temp.next and temp.next.val==val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return head
        