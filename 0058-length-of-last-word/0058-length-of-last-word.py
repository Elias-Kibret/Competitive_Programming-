class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        N=len(s)-1
        count=0
        while s[N]==" ":
            N-=1
        while N>=0 and s[N]!=" ":
            count+=1
            N-=1
        return count
            

