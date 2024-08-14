class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs=sorted(strs)
        index=0
        prefix=""

        while index<len(strs[0]) and index<len(strs[-1]):
            if strs[0][index]==strs[-1][index]:
                prefix+=strs[0][index]
                index+=1
            else:
                return prefix
        return prefix
        



        
      
        
        
        
        


        