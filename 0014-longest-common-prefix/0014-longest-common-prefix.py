class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix=strs[0]
        index=0
        pre=""

        for i in range(len(prefix)):
            for val in strs[1:]:
                
                if len(val)==i or val[i]!=prefix[i]:
                    return pre
            pre+=prefix[i]
        return pre

            

        
        return ""
    
        

      
        
        
        
        


        