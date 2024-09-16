class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        s=set()

        res=[]

        for val in nums:
            if val in s:
                res.append(val)
            else:
                s.add(val)
        return res