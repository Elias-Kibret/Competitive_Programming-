class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasingStack=[nums[0]]
        decreasingStack=[nums[0]]


        for i in range(1,len(nums)):
            if nums[i]>=decreasingStack[-1] and nums[i]>=increasingStack[-1]:
                increasingStack.append(nums[i])
            if nums[i]<=increasingStack[-1] and nums[i]<=decreasingStack[-1]:
                decreasingStack.append(nums[i])
        print(increasingStack,decreasingStack)
    
        return len(increasingStack)==len(nums) or len(decreasingStack)==len(nums) 


        
        