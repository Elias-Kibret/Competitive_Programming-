# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        res=ListNode(0)
        temp2=res
        nums=set(nums)
        while temp:
            if temp.val not in nums:
                temp2.next=ListNode(temp.val)
                temp2=temp2.next    
            temp=temp.next
        return res.next


        