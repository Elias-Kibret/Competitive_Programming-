class Solution:
    def fib(self, n: int) -> int:

        self.table=[-1]*(n+1)
        return self.recDpFib(n)
        



    def recDpFib(self,n):
        print(self.table)
        if self.table[n]<0:
            if n==0 or n==1:
                self.table[n]=n
            else:
                self.table[n]=self.recDpFib(n-2)+self.recDpFib(n-1)
        return self.table[n]
        