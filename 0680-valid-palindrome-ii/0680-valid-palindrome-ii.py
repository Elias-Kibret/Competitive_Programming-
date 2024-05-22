class Solution:
    def validPalindrome(self, s: str) -> bool:
        # left,right=0,len(s)-1
        # skiped=False

        # while left<right:
        #     if s[left]!=s[right] and s[left+1]!=s[right] and s[left]!=s[right-1]:
        #         return False
        #     left+=1
        #     right-=1
        # return True

        def verify(s,left,right,deleted):
            while left<right:
                if s[left]!=s[right]:
                    if deleted:
                        return False
                    else:
                        return verify(s,left+1,right,True) or verify(s,left,right-1,True)
                else:
                    left+=1
                    right-=1
            return True
        return verify(s,0,len(s)-1,False)
        


        