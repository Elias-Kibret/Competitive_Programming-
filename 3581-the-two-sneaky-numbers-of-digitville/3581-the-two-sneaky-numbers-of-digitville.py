class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
       
        res=[]

        for key, val in count.items():
            if val>1:
                res.append(key)
        return res

        