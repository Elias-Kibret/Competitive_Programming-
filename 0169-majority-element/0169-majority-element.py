class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        N=len(nums)/2
        countNums=Counter(nums)
        mx=0

        for val in countNums.keys():
            if countNums[val]>=N:
                mx=val
        return mx

    


       
        
        
        
                
            
                

        
        