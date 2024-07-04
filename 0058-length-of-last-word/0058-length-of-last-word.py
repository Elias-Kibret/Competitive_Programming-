class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        lastCharIndex=len(s)-1
        count=0

        for i in range(len(s)-1,-1,-1):
            if s[i]!=' ':
                lastCharIndex=i
                break
        

        for i in range(lastCharIndex,-1,-1):
            if s[i]!=' ':
                count+=1
            else:
                return count
        return count


   

        
       

        




                
        