class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        writeIndex=0
        readIndex=0
        N=len(nums)

        while writeIndex<N and readIndex<N:
            if nums[writeIndex]==val and nums[readIndex]!=val:
                nums[writeIndex],nums[readIndex]=nums[readIndex],nums[writeIndex]
                writeIndex+=1
            elif nums[writeIndex]!=val:
                writeIndex+=1
            readIndex+=1
            
        print(nums)
        return writeIndex

       