class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        firstCharIndex=len(s)-1
        count=0

        for i in range(len(s)-1,-1,-1):
            if s[i]!=' ':
                firstCharIndex=i
                break
        for i in range(firstCharIndex,-1,-1):
            if s[i]!=' ':
                count+=1
            else:
                return count
        return count


   

        
       

        




                
        