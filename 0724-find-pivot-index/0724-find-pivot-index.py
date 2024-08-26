class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(0+num for num in nums)
        rightSum,leftSum=0,0
        for index, num in enumerate(nums):
            rightSum=total-leftSum-num
            if rightSum==leftSum:
                return index
            leftSum+=num 
        return -1

     

       