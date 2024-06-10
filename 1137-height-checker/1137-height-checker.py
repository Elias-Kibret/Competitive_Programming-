class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        return  sum(h1!=h2 for h1,h2 in zip(sorted(heights),heights))
        

       



        
        