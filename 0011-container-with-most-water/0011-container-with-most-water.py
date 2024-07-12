class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)<2:
            return 0

        l,r=0,len(height)-1
        max_water=0
        
        while l<r:
            
            max_water=max(max_water,(r-l)*(min(height[l],height[r])))
            print(min(height[l],height[r]))
            if height[r]>height[l]:
                l+=1
            elif height[r]<height[l]:
                r-=1
            else:
                r-=1
                l+=1
        return max_water

        
