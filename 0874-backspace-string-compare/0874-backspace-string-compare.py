class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def remove(st:str)->str:
            stack=[]
            for val in st:
                if stack and val=="#":
                    stack.pop()
                elif val!='#':
                    stack.append(val)
            return "".join(stack)
        return remove(s)==remove(t)
            
        