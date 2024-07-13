class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]

        for val in num:
            while k>0 and stack and stack[-1]>val:
                k-=1
                stack.pop()
            stack.append(val)
        stack=stack[:len(stack)-k]
        res=''.join(stack).lstrip('0')
        return ''.join(stack).lstrip('0') if res else "0"
        
                

        
        

        
       
            
            
        