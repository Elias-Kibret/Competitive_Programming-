class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count=[0]*26

        for c in s:
            count[ord(c)-ord('a')]+=1
        for c in t:
            count[ord(c)-ord('a')]-=1
        for i in range(26):
            if count[i]!=0:
                return False
        return True
        
        # if len(s) != len(t):
        #     return False
        
        # for char in string.ascii_lowercase:
        #     if s.count(char) != t.count(char):
        #         return False
        # return True