# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findLength(self,head:Optional[ListNode]) -> int:
        size=0
        temp=head
        while temp:
            size+=1
            temp=temp.next
        return size


    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        size=self.findLength(head)

        base_size=size//k
        extra_nodes=size%k

        result=[None]*k

        current=head
        prev=None


        for i in range(k):
            result[i]=current
            part_size=base_size + (1 if extra_nodes>0 else 0)

            for j in range(part_size):
                prev=current
                current=current.next
            if prev:
                prev.next=None
            extra_nodes-=1
        return result
              

        # res=[]
        # if  k>size:
        #     res=[1]*size+[0]*(k-size)
        # else:
        #     temp=size//k
        #     res=[temp]*k

        # mod=size%k
       
        # index=0
        # while mod>0 and k<size:
        #     res[index]+=1
        #     index+=1
        #     mod-=1
        # result=[]
        # temp=head
        
        # for val in res:
        #     curr_head=ListNode(0)
        #     cur=curr_head
            
        #     for i in range(val):
        #         cur.next=ListNode(temp.val)
        #         temp=temp.next
        #         cur=cur.next
        #     result.append(curr_head.next)
        # return result
        