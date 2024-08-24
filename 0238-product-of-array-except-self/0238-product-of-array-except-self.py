class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        countZero=0
        for val in nums:
            if val==0:
                countZero+=1
        res=[0]*len(nums)
        if countZero>1:
            return [0]*len(nums)
        product=1

        for val in nums:
            if val!=0:
                product*=val
        for i in range(len(nums)):
            if countZero==1 and nums[i]!=0:
                res[i]=0
            elif nums[i]==0 and countZero==1:
                res[i]=product
            else:
                res[i]=product//nums[i]
           

            
        return res

     

     
        
            
    