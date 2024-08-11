class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        m=set({x for x in range(1,len(nums)+1)})
        res=[]

        for val in nums:
            if val in m:
                m.remove(val)
            else:
                res.append(val)
        res.append(m.pop())
        return res
        
            
        
        