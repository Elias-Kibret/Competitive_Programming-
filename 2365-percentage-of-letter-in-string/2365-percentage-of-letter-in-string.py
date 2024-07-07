class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count=0

        for val in s:
            if val==letter:
                count+=1
        return int(count/len(s)*100)
        