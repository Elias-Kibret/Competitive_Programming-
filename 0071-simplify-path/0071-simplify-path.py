class Solution:
    def simplifyPath(self, path: str) -> str:

        stack=[]
        parts=path.split('/')

        for part in parts:
            if stack and part=='..':
                stack.pop()
            elif part not in {'.','','..'}:
                stack.append(part)
        return "/"+"/".join(stack)
        
                
            
           
                
                

        