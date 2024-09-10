# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd (self,a,b) -> int :
        while b!=0:
            a,b=b,a%b
        return a

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        
        # res=ListNode(0)
        # res_temp=res
        # temp=head

        # while temp:
        #     res_temp.next=ListNode(temp.val)
        #     res_temp=res_temp.next
        #     if temp.next:
        #         print(gcd(temp.val,temp.next.val))
        #         res_temp.next=ListNode(self.gcd(temp.val,temp.next.val))
        #         res_temp=res_temp.next
        #     temp=temp.next
        # return res.next

        cur=head

        while cur.next:
            n1,n2=cur.val,cur.next.val
            cur.next=ListNode(self.gcd(n1,n2),cur.next)
            cur=cur.next.next
        return head
            
        
                
        