class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total=0


        for i in range(len(nums)-1):
            min_val=nums[i]
            max_val=nums[i]
                    
        
            for j in range(i+1, len(nums)):
                min_val=min(min_val,nums[j])
                max_val=max(max_val,nums[j])
                total+=max_val-min_val
        return total
        