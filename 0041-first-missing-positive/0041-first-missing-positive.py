class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mp={}
        
        for index,val in enumerate(nums):
            mp[val]=index
        mx=max(nums)
        
        for val in range(1,mx):
            if val not in mp:
                return val
            
        return mx+1 if mx>=0 else 1
        