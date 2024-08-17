class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:     
        write=0
        N=len(nums)
        for read in range(N):
            if nums[read]!=val and nums[write]==val:
                nums[read],nums[write]=nums[write],nums[read]
                write+=1
            if nums[write]!=val:
                write+=1
        return write


    

       