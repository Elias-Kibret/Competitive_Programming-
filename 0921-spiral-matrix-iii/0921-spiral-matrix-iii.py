class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions=[[0,1],[1,0],[0,-1],[-1,0]]

        res=[]

        r,c=rStart,cStart
        steps=1


        #switchDirection
        i=0
        



        while len(res)<rows*cols:
            '''
             Right=1
             Down=1

             Left=2
             Up=2

             Right=3
             Down=3

             Left=4
             Up=4

             so we need to loop twice to get this algorithm

            '''
            for _ in range(2):

                '''
                  switch direction
                '''
                dr,dc=directions[i]

                for _ in range(steps):
                    if (0<=r<rows and 0<=c<cols):
                        res.append([r,c])

                    '''
                    add to row and col 
                    '''
                    r,c=r+dr,c+dc

                '''
                 this importan Focus , which used to switch direction 
                 and the module 4 (%4) used to keep in the direction 
                '''
                i=(i+1)%4
            '''
            rememebr steps update after twice loop
            '''
            steps+=1
        return res


        