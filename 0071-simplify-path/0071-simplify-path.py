class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")
        
        
        stack=[]

        for val in parts:

            if not stack:
                stack.append('/')
                continue
            elif val not in {'..','.',''}:
                stack.append(val)
                stack.append('/')

            elif val=='..' and len(stack)>=2:
                stack.pop()
                stack.pop()
        if len(stack)>1 and stack[-1]=='/':
            stack.pop()
        return "".join(stack)
       




        
            
                
            
           
                
                

        