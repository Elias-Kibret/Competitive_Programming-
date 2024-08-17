class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        res=[[1]]
        for numRow in range(2,numRows+1):
            result=[1]*numRow
            for i in range(1,numRow-1):
                result[i]=res[-1][i-1]+res[-1][i]
            res.append(result)
        return res

        