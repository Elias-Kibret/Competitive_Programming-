# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        There are two apporaches to 
        solve this problem

        The first one is iterative 
        the second one is Recusive
        
        for iterative
        Time complexity max(len(l1,l2))
        Space complexity max(len(11,l2))

        '''

        result=ListNode(None)
        temp=result
        L1=l1
        L2=l2
        carry=0

        while L1 or L2:
    
            current_sum=(L1.val if L1 else 0 )+(L2.val if L2 else 0)+carry
            
            carry=current_sum//10
            quotient=current_sum%10 if current_sum>9 else current_sum

            temp.next=ListNode(quotient)
            L1=L1.next if L1 else None
            L2=L2.next if L2 else None
            temp=temp.next
        if carry!=0:
            temp.next=ListNode(carry)
        return result.next
            
            
        