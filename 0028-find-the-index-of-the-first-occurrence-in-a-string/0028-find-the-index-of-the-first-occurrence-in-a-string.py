class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # found=False

        
        # follow_ptr=0

        # check_ptr=0

        # while check_ptr<len(haystack):
        #     if haystack[check_ptr]==needle[follow_ptr]:
        #         while follow_ptr<len(needle) and check_ptr<len(haystack):
        #             if haystack[check_ptr]==needle[follow_ptr]:
        #                 follow_ptr+=1
                        
        #             else:
             
        #                 follow_ptr=0
        #                 break
        #             check_ptr+=1
                
                
        #     else:
        #         check_ptr+=1
        #     if len(needle)==follow_ptr:
        #         return check_ptr-follow_ptr
        # return -1
        if len(haystack)<len(needle):
            return -1



        index=[]

        for i in range(len( haystack)):
            if haystack[i]==needle[0]:
                index.append(i)
        for val in index:
            ptr=0
            check_ptr=val

            while ptr<len(needle) and check_ptr<len(haystack) and haystack[check_ptr]==needle[ptr] :
                ptr+=1
                check_ptr+=1
            if ptr==len(needle):
                return val
        return -1


            
                    

