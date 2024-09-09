class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==0:
            return []

        result=[]
        i,j=0,-1
        direction=1
        C=len(matrix[0])
        R=len(matrix)
        N=C*R
        
        while len(result)<N:

            for _ in range(C):
                j+=direction
                result.append(matrix[i][j])
            R-=1

            for _ in range(R):
                i+=direction
                result.append(matrix[i][j])
            C-=1
            direction*=-1


        return result
        # if len()

        # while 
        