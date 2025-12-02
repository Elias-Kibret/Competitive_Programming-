class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maxLength=0
        

        # for i in range(len(s)):
        #     checkDuplicate=set()
        #     duplicateFound = false
        #     for j in range(i,len(s)):
        #         if s[j] in  checkDuplicate:
        #             maxLength=max(maxLength,j-i)
        #             break
        #         else:
        #             checkDuplicate.add(s[j])
        # return maxLength
        left=0
        check=set()
        longestSubstring=0
        '''
        we keep adding letters to the set and if we there is char , we increment our left pointer
        '''

        for right in range(len(s)):
            while s[right] in check:
                check.remove(s[left])
                left+=1
            check.add(s[right])
            longestSubstring=max(longestSubstring,right-left+1)
        return longestSubstring

  




            

        
            
                
                
            
                
    
                

                   
