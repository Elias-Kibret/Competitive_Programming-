class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # nums.sort()

        # l,r,count=0,len(nums)-1,0

        # while(l<r):
        #     if(nums[l]+nums[r]==k):
        #         count+=1
        #         l+=1
        #     elif (nums[l]+nums[r]>k):
        #         r-=1
        #     else:
        #         l+=1
        # return count
        count=0

        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if(abs(nums[i]-nums[j])==k):
                    count+=1
        return count