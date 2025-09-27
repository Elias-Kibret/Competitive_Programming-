class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_sorted=sorted(s)
        t_sorted=sorted(t)


        for index in range(len(s_sorted)):
            if s_sorted[index]!=t_sorted[index]:
                return False
        return True
 
        