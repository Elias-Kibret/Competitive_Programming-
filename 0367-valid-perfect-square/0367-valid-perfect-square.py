class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left,right=0,num

        while left<=right:
            mid=(left+right)//2

            if mid*mid==num:
                return True
            if mid*mid>num:
                right=mid-1
            else:
                left=mid+1
        return False
        

        
        