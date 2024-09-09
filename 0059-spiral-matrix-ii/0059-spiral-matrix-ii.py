class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        '''
         we have n^2 elements 

        '''
        N=n*n
        C,R=n,n

        """
        Whenever we have sparila matrix , we need 3 thing

          1] pointer to track row 
          2] pointer to track column
          3] pointer to track direction

        """
        i=0
        j=-1
        direction=1

        '''
         Intialise a matrix to hold result

        '''
        matrix=[[-1]*n for _ in range(n)]

        '''
        Value we gonna set in the matrix 
        '''
        value=1

        
        while value<=N:
            for _ in range(C):
                j+=direction
                matrix[i][j]=value
                value+=1
            R-=1

            for _ in range(R):
                i+=direction
                matrix[i][j]=value
                value+=1
            C-=1
            direction*=-1
        return matrix