# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result=0
        current=head
       
        
        
        while current is not None:
            
            result=result<<1 | current.val
            current=current.next
   
        return result
        