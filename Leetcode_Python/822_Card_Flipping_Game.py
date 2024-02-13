# https://leetcode.com/problems/card-flipping-game/description/


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        # fronts_map={value:index for index,value in enumerate(fronts)}
        # back_map={value:index for index ,value in enumerate(backs)}
        # result=[]
        # for value in backs:
        #     if value not in fronts_map:
        #         result.append(value)
        # for value in fronts:
        #     if value not in back_map:
        #         result.append(value)
        # if len(result)==0:
        #     return 0
        
        # return min(result)
        
        s = set(fronts + backs)
        for i in range(len(fronts)):
            if fronts[i] == backs[i] and fronts[i] in s:
                 s.remove(fronts[i])
        if len(s) == 0:
            return 0
        return min(s)
            
        
        
            
                






        