# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l=0
        temp=head
        while temp:
            l+=1
            temp=temp.next    
        res=[]
        if  k>l:
            res=[1]*l+[0]*(k-l)
        else:
            temp=l//k
            res=[temp]*k

        mod=l%k
       
        index=0
        while mod>0 and k<l:
            res[index]+=1
            index+=1
            mod-=1
        result=[]
        temp=head
        
        for val in res:
            curr_head=ListNode(0)
            cur=curr_head
            
            for i in range(val):
                cur.next=ListNode(temp.val)
                temp=temp.next
                cur=cur.next
            result.append(curr_head.next)
        return result
        