class Solution:
    def mySqrt(self, x: int) -> int:
        left,right=0,x

        while left<=right:
            md=(left+right)//2

            if md*md==x:
                return md
            elif md*md>x:
                right=md-1
            else:
                left=md+1
        return right
        
        