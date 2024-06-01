class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        left,max_length,numOfVowels=0,0,0

        vowels={"a","e","i","o","u"}

        for right in range(len(s)):

            if s[right] in vowels:
                numOfVowels+=1
            if right-left+1==k:
                max_length=max(max_length,numOfVowels)
                if s[left] in vowels:
                    numOfVowels-=1
                left+=1
        return max_length



        