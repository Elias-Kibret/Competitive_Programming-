# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # result=ListNode(0)
        # tail=result
        # carry=0

        # while l1  or l2  or carry!=0:
        #     val1=l1.val if l1 else 0
        #     val2=l2.val if l2 else 0
        #     total=carry+val1+val2
        #     value=total%10
        #     carry=total//10
        #     tail.next=ListNode(value)
        #     tail=tail.next
        #     l1=l1.next if l1 else None
        #     l2=l2.next if l2 else None
        # return result.next
        return self.add(l1,l2,0)

        
    def add(self, l1: Optional[ListNode], l2: Optional[ListNode],carry:int) -> Optional[ListNode]:
        if l1 is None and l2 is None and carry==0:
            return None
        val1=l1.val if l1 else 0
        val2=l2.val if l2 else 0

        total=val1+val2+carry
        newDigit=total%10
        carry=total//10

        newNode=ListNode(newDigit)
        print(newNode)
        newNode.next=self.add(l1.next if l1 else None , l2.next if l2 else None,carry)
        return newNode
        