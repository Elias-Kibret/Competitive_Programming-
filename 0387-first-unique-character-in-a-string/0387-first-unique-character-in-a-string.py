class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap=Counter(s)
        
        for i in range(len(s)):
            if hashMap[s[i]]==1:
                return i
        return -1
        