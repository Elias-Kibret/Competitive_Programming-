class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        mod=k%sum(0+x for x in chalk)
     
        for index,value in enumerate(chalk):
            if mod-value<0:
                return index
            mod-=value
        
        return 1
        