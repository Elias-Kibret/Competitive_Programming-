# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result=[]

        for val in lists:
            cur=val

            while cur:
              
                result.append(cur.val)
                cur=cur.next
        result.sort()
        
        n=ListNode(0)
        temp=n
        for val in result:
            temp.next=ListNode(val)
            temp=temp.next
  
        return n.next
    
        