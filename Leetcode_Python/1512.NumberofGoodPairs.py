class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        if len(nums)<1 or len(nums)>100:
            print("Invalid Input")
        count=0
        
        for index, value in enumerate(nums):
            for second_index in range(index+1,len(nums)):
                if value==nums[second_index]:
                    count+=1
        return count
