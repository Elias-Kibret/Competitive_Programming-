class Solution:
    def countSubstrings(self, s: str) -> int:

        result=0

        for pos in range(0,len(s)):
            left,right=pos,pos

            while left>=0 and right<len(s) and s[left]==s[right]:
                result+=1
                left-=1
                right+=1
            left,right=pos,pos+1
            
            while left>=0 and right<len(s) and s[left]==s[right]:
                result+=1
                left-=1
                right+=1
        return result
        