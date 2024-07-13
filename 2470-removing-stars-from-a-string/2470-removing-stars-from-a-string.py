class Solution:
    def removeStars(self, s: str) -> str:

        stack=[]

        for val in s:
            if not stack and val!='*':
                stack.append(val)
            elif val=="*":
                stack.pop()
            else:
                stack.append(val)
        return "".join(stack)
            
        