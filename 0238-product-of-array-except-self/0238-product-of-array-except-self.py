class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=prod([x for x in nums if x!=0])
        count_zero=sum(1 for x in nums if x==0 )
        is_zero=True if 0 in nums else False

        res=[0]*len(nums)

        if count_zero>1:
            return res

        for index,val in enumerate(nums):
            if is_zero:
                if val==0:
                    res[index]=product
                else:
                    res[index]=0
            else:
                res[index]=product//val
        return res
                



      
       
        