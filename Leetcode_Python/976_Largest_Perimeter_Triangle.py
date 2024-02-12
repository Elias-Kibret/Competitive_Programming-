# https://leetcode.com/problems/largest-perimeter-triangle/description/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        perimeter=0
        print(nums)
        for index in range(len(nums)-2):
            print(nums[index],nums[index+1],nums[index+2])

            if nums[index]<nums[index+1]+nums[index+2]:
                perimeter=max(perimeter,nums[index]+nums[index+1]+nums[index+2])
        return perimeter
