class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        res=0
        count={}

        for num in nums:
            if num in count:
                res+=count[num]
            count[num]=1+count.get(num,0)
        
        return res