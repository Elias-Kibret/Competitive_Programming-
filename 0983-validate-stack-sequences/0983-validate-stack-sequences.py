class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed)!=len(popped):
            return False
        stack=[]
        index=0

        for val in pushed:
            stack.append(val)

            while stack and index<len(popped) and stack[-1]==popped[index]:
                index+=1
                stack.pop()
        return len(stack)==0
        