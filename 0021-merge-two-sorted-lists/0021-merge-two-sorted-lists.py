# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        listNode=ListNode()
        temp=listNode

        while list1 and list2:
            if list1.val<list2.val:
                temp.next=ListNode(list1.val)
                list1=list1.next
            else:
                temp.next=ListNode(list2.val)
                list2=list2.next
            temp=temp.next
            
        if list1 or list2:
            temp.next=list1 if list1 else list2
      
        print(listNode.next)
        return listNode.next
        