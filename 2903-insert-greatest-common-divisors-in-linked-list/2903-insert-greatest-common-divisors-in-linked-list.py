# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode(0)
        res_temp=res
        temp=head

        while temp:
            res_temp.next=ListNode(temp.val)
            res_temp=res_temp.next
            if temp.next:
                print(gcd(temp.val,temp.next.val))
                res_temp.next=ListNode(math.gcd(temp.val,temp.next.val))
                res_temp=res_temp.next
            temp=temp.next
        return res.next
            
        
                
        