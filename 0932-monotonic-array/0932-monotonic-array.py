class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc,dec=True,True

        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                inc=False
            elif nums[i]>nums[i-1]:
                dec=False
        return dec or inc

       

       
       

        
        