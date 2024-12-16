class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]

        count=0

        for val in s:
            if val=="(":
                stack.append('(')
            elif stack:
                stack.pop()
            else:
                count+=1
        return count+len(stack)
        