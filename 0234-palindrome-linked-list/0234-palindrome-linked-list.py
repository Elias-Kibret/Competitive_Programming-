# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # fist I have to reverse the linkedin list then 
        # I will loop through each linkedin list at the same time and compare the value
        #  the time complexity is would be O(n) and the space complexity is O(n)

        # reverse linkedin list
        if not head :
            return False

        # Step 1: find the middle of the linked list
        slow=head
        fast=head

        # use fast and slow pointers to find the middle of the list

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next


        #step2 : reverse the second half of the list

        second_half=None

        while slow:
            next=slow.next
            slow.next=second_half
            second_half=slow
            slow=next
        #step3 : Compare the fist and second half nodes
        first_half=head
 
        while second_half:
            if first_half.val!=second_half.val:
                return False
            first_half=first_half.next
            second_half=second_half.next
        return True
        


        
        
      
        
        
       


        