class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N=len(nums)
        l,r=0,N-1

        res=N*[0]
        position=N-1

        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                res[position]=nums[l]*nums[l]
                l+=1
            else:
                res[position]=nums[r]*nums[r]
                r-=1
            position-=1
        return res

        