class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mx=max(nums)
        mn=min(nums)
        
        while mx!=0:
            mn,mx=mx,mn%mx
        return mn
        