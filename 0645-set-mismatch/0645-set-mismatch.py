class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        numSet=set({x for x in range(1,len(nums)+1)})
        print(numSet)
        res=[]

        for val in nums:
            if val in numSet:
                numSet.remove(val)
            else:
                res.append(val)
        value=numSet.pop()
        res.append(value)
        return res

       
        
            
        
        