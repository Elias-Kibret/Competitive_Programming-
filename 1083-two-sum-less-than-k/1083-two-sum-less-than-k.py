class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # result=-1

        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         summedNumbers=nums[i]+nums[j]
        #         if summedNumbers>result and summedNumbers<k:
        #             result=summedNumbers
        # return  result

        nums.sort()
        '''
        pointers
        '''
        left,right=0,len(nums)-1
        result=-1

        while left<right:
            summed=nums[left]+nums[right]
            if summed>=k:
                right-=1
                continue
            if summed<k and summed>result:
                result=summed
            left+=1
        return result
            


        