class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={'a','e','i','o','u'}

        max_count,current_count=0,0

        for i in range(k):
            if s[i] in vowels:
                current_count+=1
        max_count=current_count

        for r in range(k,len(s)):
            if s[r] in vowels:
                current_count+=1
            if s[r-k] in vowels:
                current_count-=1
            max_count=max(max_count,current_count)
        return max_count
