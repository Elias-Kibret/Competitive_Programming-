class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows<1:
            return [[]]
        result=[[1]]

        for numRow in range(2,numRows+1):
            res=[1]*numRow

            for i in range(1,numRow-1):
                
                res[i]=result[-1][i]+result[-1][i-1]
            result.append(res)
        
        return result
          