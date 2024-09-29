class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        # else:
        #    return self.fib(n-1) + self.fib(n-2)
        pre=0
        cur=1

        for i in range(2,n+1):
            temp=cur+pre
            pre,cur=cur,temp
        return cur
        
        