# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        '''
        The time complexity is O(n)
        where n is the length of linkedList

        The space compexity would be O(N)

        '''


        '''
        so what I will do it is 
        I will loop through the linkedin list 
        till the end

        
        '''

        current=head

        prev=None

        while current:
            newNode=current.next
            current.next=prev

            prev=current
            current=newNode

        return prev




        