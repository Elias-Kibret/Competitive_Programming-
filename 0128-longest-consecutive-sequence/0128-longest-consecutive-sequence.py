
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        res=0
        for num in nums:
            if num-1 not in nums_set:
                count=0
                while num+count in nums_set:
                    count+=1
                res=max(res,count)           
        return res


        