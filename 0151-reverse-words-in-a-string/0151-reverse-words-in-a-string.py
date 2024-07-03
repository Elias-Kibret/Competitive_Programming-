class Solution:
    def reverseWords(self, s: str) -> str:
        # clean leading and trailin spaces
        s=s.strip()
        word=""
        stack=[]

        for index in range(len(s)):
            if s[index]!=" ":
                word+=s[index]
            
            elif len(word)!=0:
                stack.append(word)
                word=""
            if index==len(s)-1:
                stack.append(word)
        st=''
        print(stack)
        while stack:
            st+=stack.pop()
            if stack:
                st+=' '
                
            
        return st
        
        
                


    

  

        
                

       


