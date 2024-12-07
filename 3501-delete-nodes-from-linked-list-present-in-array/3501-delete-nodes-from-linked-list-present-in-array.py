# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        
        
        result=ListNode(0)
        temp_result=result

        nums_set=set(nums)

        while temp:
            if temp.val not in nums_set:
                temp_result.next=ListNode(temp.val)
                temp_result=temp_result.next
                
            temp=temp.next
        return result.next
         
    
        