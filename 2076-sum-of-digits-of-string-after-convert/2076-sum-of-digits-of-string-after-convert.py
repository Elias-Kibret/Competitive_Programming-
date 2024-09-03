class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # temp=""
        # for val in s:
        #     temp+=str((ord(val)-96))
        # N=len(temp)
        # temp=int(temp)
        # while k>0:
        #     res=0
        #     for _ in range(N):
               
        #         res+=temp%10
        #         temp=temp//10
        #     temp=res
        #     k-=1
        # return res
        converted=self.convert(s)
        result=converted

        for i in range(k):
            result=self.getSum(result)
        return int(result)


    def convert(self,s):
        converted=""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for char in s:
            converted+=str(alphabet.index(char)+1)
        return converted
        
    def getSum(self,converted):
        result=0
        for char in str(converted):
            result+=int(char)
        return str(result)
        