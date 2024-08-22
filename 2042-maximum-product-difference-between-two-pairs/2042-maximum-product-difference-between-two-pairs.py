class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        if len(nums)<4:
            return 0
        nums.sort()

        return (nums[-1]*nums[-2])-(nums[0]*nums[1])
        

    
