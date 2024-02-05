
class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        left, right=0, len(s)-1
        vowels = "aeiouAEIOU"
        while left<right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left+=1
                right-=1
            elif s[left] not in vowels:
                left+=1
            elif s[right] not in vowels:
                right-=1
        return ''.join(s)
                                    #  Elias Kibret



# 345. Reverse Vowels of a String
# Solved
# Easy
# YouTube
# Topics
# Companies
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"
 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.