class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        # left,max_length,numOfVowels=0,0,0

        # vowels={"a","e","i","o","u"}

        # for right in range(len(s)):

        #     if s[right] in vowels:
        #         numOfVowels+=1
        #     if right-left+1==k:
        #         max_length=max(max_length,numOfVowels)
        #         if s[left] in vowels:
        #             numOfVowels-=1
        #         left+=1
        # return max_length


        vowels={"a","e","i","o","u"}

        max_vowels=0
        current_vowels=0

        for i in range(k):
            if s[i] in vowels:
                current_vowels+=1
        max_vowels=current_vowels

        for i in range(k,len(s)):
            if s[i] in vowels:
                current_vowels+=1
            if s[i-k] in vowels:
                current_vowels-=1
            max_vowels=max(max_vowels,current_vowels)
        return max_vowels



        