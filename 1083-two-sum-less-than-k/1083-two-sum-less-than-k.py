class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        result=-1

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                summedNumbers=nums[i]+nums[j]
                if summedNumbers>result and summedNumbers<k:
                    result=summedNumbers
        return  result

        