class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # mp=Counter(nums)

        # for num in nums:
        #     if mp[num]==1:
        #         return num
        ans=nums[0]
        for i in range(len(nums)):
            if (i==0 and i+1<len(nums) and nums[i]!=nums[i+1]) or( i==len(nums)-1 and nums[i-1]!=nums[i]):
                ans= nums[i]
            elif i+1<len(nums) and nums[i]!=nums[i+1] and i>=0 and  nums[i]!=nums[i-1]:
                ans=nums[i]
        return ans


    

    
        
            
        
            
    
        
