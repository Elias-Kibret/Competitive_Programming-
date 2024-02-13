# https://leetcode.com/problems/reverse-words-in-a-string/description/

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
      
        
        