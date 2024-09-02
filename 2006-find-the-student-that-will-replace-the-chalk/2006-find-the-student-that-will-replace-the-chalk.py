class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        mod=k%sum(chalk)
     
        for index,value in enumerate(chalk):
            if mod-value<0:
                return index
            mod-=value
        
        return -1
        