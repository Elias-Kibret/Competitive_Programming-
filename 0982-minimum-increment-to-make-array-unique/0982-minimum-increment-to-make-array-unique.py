class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        l,r=0,1
        count=0
        while r<len(nums):
            if nums[l]==nums[r]:
                nums[r]=nums[r]+1
                count+=1
            elif nums[l]>nums[r]:
                count+=nums[l]-nums[r]+1
                nums[r]=nums[l]+1
                
            r+=1
            l+=1
        print(nums)
        return count
            

       