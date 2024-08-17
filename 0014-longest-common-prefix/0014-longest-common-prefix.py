class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        s=""
        pt=0

        while pt<len(strs[0]) and pt<len(strs[-1]):
            if strs[0][pt]==strs[-1][pt]:
                s+=strs[0][pt]
                pt+=1
            else:
                break
        return s

        
      
        
        
        
        


        