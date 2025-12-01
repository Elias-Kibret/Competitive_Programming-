class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        longestSubstring=0
        


        for i in range(len(s)):
            check=set()
            duplicate=False
            for j in range(i,len(s)):
                check.add(s[j])
                if len(check)>2:
                    longestSubstring=max(longestSubstring,j-i)
                    duplicate=True
                    break
            if not duplicate:
                longestSubstring=max(longestSubstring,len(s)-i)

                
        return longestSubstring
