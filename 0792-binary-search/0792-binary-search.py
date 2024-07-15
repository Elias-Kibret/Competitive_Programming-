class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary(start:int,end:int):
            if start>=end:
                return -1
            m=(start+end)//2
            if nums[m]==target:
                return m
            elif nums[m]<target:
                return binary(m+1,end)
            else:
                return binary(start,m)
            

        return binary(0,len(nums))


        