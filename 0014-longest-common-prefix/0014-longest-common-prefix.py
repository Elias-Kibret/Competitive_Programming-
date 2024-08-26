class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        s.sort()

        strs=""
        index=0
        minN=min(len(s[0]),len(s[-1]))

        while True:
            if index<minN and s[0][index]==s[-1][index]:
                strs+=s[0][index]
                index+=1
            else:
                return strs
        return strs
        
       

        
      
        
        
        
        


        