class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result=""
        j=0
        while j<len(s):
            total=0
            i=0
            while i<k:
                total+=ord(s[j])-ord("a")
                j+=1
                i+=1
           
            result+=chr(total%26+ord("a"))
        
        return result
        


        