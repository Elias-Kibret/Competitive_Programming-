class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        N=n*n
        C,R=n,n
        i=0
        j=-1
        direction=1
        matrix=[[-1]*n for _ in range(n)]
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