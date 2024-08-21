class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # if rowIndex==0:
        #     return [1]
        # result=[[1]]

        # for numrow in range(2,rowIndex+2):
        #     res=[1]*numrow
        #     for i in range(1,numrow-1):
        #         res[i]=result[-1][i]+result[-1][i-1]
        #     result.append(res)
        # return result[-1]

        row=[1]*(rowIndex+1)

        for i in range(1,rowIndex):
            for j in range(i,0,-1):
                row[j]+=row[j-1]
        return row

        