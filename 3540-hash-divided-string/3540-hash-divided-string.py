class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result=""
        
        # while j<len(s):
        #     total=0
        #     i=0
        #     while i<k:
        #         total+=ord(s[j])-ord("a")
        #         j+=1
        #         i+=1
           
        #     result+=chr(total%26+ord("a"))
        
        # return result
        prefix=0

        for index,ch in enumerate(s):
            prefix+=ord(ch)-97

            if (index+1)%k==0:
                result+=chr(97+prefix%26)
                prefix=0
        return result

        


        