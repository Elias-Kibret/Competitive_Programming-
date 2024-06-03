class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_left=0
        t_left=0
        while s_left<len(s) and t_left<len(t):
            if s[s_left]==t[t_left]:
                t_left+=1
            s_left+=1
        return len(t)-t_left

        

      

       



        