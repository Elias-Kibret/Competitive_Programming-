class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count_s=defaultdict(int)

        for char in s:
            count_s[char]=1+count_s.get(char,0)

        for char in t:
            if char not in count_s:
                return False
            else:
                count_s[char]-=1
                if count_s[char]==0:
                    del count_s[char]
        return len(count_s)==0
    

            
        

       

        
        