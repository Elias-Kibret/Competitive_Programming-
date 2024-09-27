class Solution:
    def findGCD(self, nums: List[int]) -> int:

        '''
        This problem is solved using Euclids Algorthim
        
        '''
        mx=max(nums)
        mn=min(nums)

        while mx!=0:
            mn,mx=mx,mn%mx
        return mn
        