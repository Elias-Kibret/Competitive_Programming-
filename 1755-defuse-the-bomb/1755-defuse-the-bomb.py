class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        decrypedCode=[0]*n

        if k==0:
            return decrypedCode
        for i in range(len(code)):
            totalSum=0
            if k>0:
                for j in range(1,k+1):
                    totalSum+=code[(i+j)%n]
            else:
                for j in range(1,abs(k)+1):
                    totalSum+=code[(i-j+n)%n]
            decrypedCode[i]=totalSum
        return decrypedCode
            




        