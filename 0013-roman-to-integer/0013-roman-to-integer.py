class Solution:
    def romanToInt(self, s: str) -> int:
        mp={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }


        i=0
        num=0

        while i<len(s):
            if i+1<len(s) and mp[s[i+1]]>mp[s[i]]:
                num+=mp[s[i+1]]-mp[s[i]]
                i+=2
            else:
                num+=mp[s[i]]
                i+=1
            
        return num


        

       