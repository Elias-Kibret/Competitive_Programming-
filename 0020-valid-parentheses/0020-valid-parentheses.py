class Solution:
    def isValid(self, s: str) -> bool:
        hash_map={")":"(","]":"[","}":"{"}
        stack=[]

        for char in s:
            if char in hash_map:
                if stack and stack[-1]==hash_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False

        
        
        