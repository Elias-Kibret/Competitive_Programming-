class Solution:
    def reverseVowels(self, s: str) -> str:
        lettersSet=('a','e','i','o','u','A','E','I','O','U')
        l,r=0,len(s)-1
        s=list(s)

        while l<r:
            if s[l] in lettersSet and s[r] in lettersSet:
                s[r],s[l]=s[l],s[r]
                l+=1
                r-=1
            else:
                if s[l] not in lettersSet:
                    l+=1
                if s[r] not in lettersSet:
                    r-=1
             
               
            
               
        return "".join(s)
    
        