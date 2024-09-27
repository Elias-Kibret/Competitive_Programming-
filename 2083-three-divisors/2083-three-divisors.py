class Solution:
    def isThree(self, n: int) -> bool:

        countFactor=2
        factor=2

        while factor<=n//2:
            if n%factor==0 :
                countFactor+=1
            factor+=1
        return True if countFactor==3 else False
        