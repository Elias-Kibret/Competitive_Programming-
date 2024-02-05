# You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# Return the string formed after mapping.

# The test cases are generated so that a unique mapping will always exist.

 

# Example 1:

# Input: s = "10#11#12"
# Output: "jkab"
# Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
# Example 2:

# Input: s = "1326#"
# Output: "acz"
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of digits and the '#' letter.
# s will be a valid string such that mapping is always possible.


class Solution:
    def freqAlphabets(self, s: str) -> str:
        result=""
        index=0
        while index<len(s):
            if index+2<len(s):
                if s[index+2]=="#":
                     result+=chr(int(s[index:index+2])+96)
                     index+=3
                else:
                    result+=chr(int(s[index])+96)
                    index+=1
            else:
                result+=chr(int(s[index])+96)
                index+=1
            
        return result