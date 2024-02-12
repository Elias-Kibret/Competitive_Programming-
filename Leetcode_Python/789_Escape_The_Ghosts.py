# https://leetcode.com/problems/escape-the-ghosts/description/



class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:        
        for value in ghosts:
            if abs(target[0]-value[0])+abs(target[1]-value[1])<=abs(target[0])+abs(target[1]):
                return False
    
        return True