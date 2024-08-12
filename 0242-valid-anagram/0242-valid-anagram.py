class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS=Counter(s)
        for val in t:
            if val not in countS:
                return False
            else:
                countS[val]=countS[val]-1 

                if countS[val]==0:
                    del countS[val]
        return len(countS)==0
        
            

            
        

       

        
        