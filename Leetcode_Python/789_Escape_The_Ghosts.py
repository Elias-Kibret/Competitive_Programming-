# https://leetcode.com/problems/escape-the-ghosts/description/



class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:        
        for value in ghosts:
            if abs(target[0]-value[0])+abs(target[1]-value[1])<=abs(target[0])+abs(target[1]):
                return False
    
        return True

# Best solution
    
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def taxi(A,B):
            return abs(A[0] - B[0]) + abs(A[1] - B[1])
        x = taxi([0,0],target)
        return all( x < taxi(g,target) for g in ghosts)
        