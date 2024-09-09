# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        matrix=[[-1]*n for _ in range(m)]

        direction=1
        i,j=0,-1

        current=head

        while current:

            for _ in range(n):
                if current:
                    j+=direction
                    matrix[i][j]=current.val
                    current=current.next
             
               
            m-=1

            for _ in range(m):
                if current:
                    i+=direction
                    matrix[i][j]=current.val
                    current=current.next
                
            n-=1
            direction*=-1
        return matrix

 
        