class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        max_num=int(sqrt(c))
        l,r=0,max_num

        while l<=r:
            ans=l**2+r**2
            if ans>c:
                r-=1
                
            elif ans<c:
                l+=1
            else:
                return True
        return False


        