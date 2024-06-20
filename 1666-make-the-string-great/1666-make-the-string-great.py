class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]

        for i in range(len(s)):
            if stack and stack[-1]!=s[i] and stack[-1].lower()==s[i].lower():
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
        




        