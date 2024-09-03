class Solution:
    def getLucky(self, s: str, k: int) -> int:
        temp=""
        for val in s:
            temp+=str((ord(val)-96))
        N=len(temp)
        temp=int(temp)
        while k>0:
            res=0
            for _ in range(N):
               
                res+=temp%10
                temp=temp//10
            temp=res
            k-=1
        return res
        