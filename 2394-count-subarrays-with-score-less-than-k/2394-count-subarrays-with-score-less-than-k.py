class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l,r=0,0
        prefix_sum=0
        ans=0
        

        while r<len(nums):
            prefix_sum+=nums[r]
            while prefix_sum*(r-l+1)>=k:
                prefix_sum-=nums[l]
                l+=1   
            ans+=(r-l+1)
                
           
            r+=1
        return ans

        