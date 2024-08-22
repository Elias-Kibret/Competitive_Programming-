class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
       
        # nums.sort()

        # return (nums[-1]*nums[-2])-(nums[0]*nums[1])

        min1=min2=float('inf')
        max1=max2=float("-inf")

        for n in nums:
            if n<=min1:
                min1,min2=n,min1
            elif n<min2:
                min2=n

            if n>=max1:
                max1,max2=n,max1
            elif n>max2:
                max2=n
        return max1*max2-min1*min2
        

    
