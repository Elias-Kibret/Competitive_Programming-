# https://leetcode.com/problems/missing-number/description/


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # nums.sort()
        # for index in range(len(nums)):
        #     if index !=nums[index]:
        #         return index
        
            
        # return len(nums)
        return sum(range(0,len(nums)+1)) - sum(nums)

        