class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        # for i in range(len(nums)-1):
        #     prefix=nums[i]
        #     for j in range(i+1,len(nums)):
        #         prefix+=nums[j]
        #         if prefix%k==0:
        #             return True
        # return False


        mod_map={0:-1}

        prefix_sum=0


        for i,n in enumerate(nums):
            prefix_sum+=n

            rem=prefix_sum%k

            if rem not in mod_map:
                mod_map[rem]=i
            elif i-mod_map[rem]>1:
                return True
        return False




































        mod_map={0:-1}

        prefix_sum=0

        for i, n in enumerate(nums):
            prefix_sum+=n

            r=prefix_sum%k

            if r not in mod_map:
                mod_map[r]=i
            elif i-mod_map[r]>1:
                return True
        return False

        