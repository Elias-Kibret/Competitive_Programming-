class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        so we are given Integer 
        which means -10^9<=nums[i]<=10^9 --
        '''
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             return True
        # return False

        nums.sort()
        print(nums)

        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False 