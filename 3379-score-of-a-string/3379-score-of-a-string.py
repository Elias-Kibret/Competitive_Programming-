class Solution:
    def scoreOfString(self, s: str) -> int:
        l=0
        r=1
        total=0
        while r<len(s):
            total+=abs(ord(s[l])-ord(s[r]))
            r+=1
            l+=1
        return total


         
        