class Solution:
    def reverse(self, x: int) -> int:
        num=x if x>0 else-1*x
        temp=num
        reverse=0
        while temp!=0:
            reverse=reverse*10+temp%10
            temp//=10
        if reverse >(2**31)-1 or reverse <-2**31:
            return 0
        return reverse if num==x else -reverse
        
