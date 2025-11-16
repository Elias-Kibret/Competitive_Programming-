class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        countZeroSubstring=0
        i=0
        countZero=0


        while i<len(nums):

            while i<len(nums) and nums[i]==0:
                countZero+=1
                i+=1
            if countZero>0:
                countZeroSubstring+=countZero*(countZero+1)//2
                countZero=0
            i+=1
        return countZeroSubstring
        