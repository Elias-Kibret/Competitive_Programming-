class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # increasingStack=[nums[0]]
        # decreasingStack=[nums[0]]


        # for i in range(1,len(nums)):
        #     if nums[i]>=decreasingStack[-1] and nums[i]>=increasingStack[-1]:
        #         increasingStack.append(nums[i])
        #     if nums[i]<=increasingStack[-1] and nums[i]<=decreasingStack[-1]:
        #         decreasingStack.append(nums[i])
        # print(increasingStack,decreasingStack)
    
        # return len(increasingStack)==len(nums) or len(decreasingStack)==len(nums) 

        if len(nums)<2:
            return True
        
        direction=0

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                if direction==0:
                    direction=1
                elif direction==-1:
                    return False
            elif nums[i]<nums[i-1]:
                if direction==0:
                    direction=-1
                elif direction==1:
                    return False
        return True


        
        