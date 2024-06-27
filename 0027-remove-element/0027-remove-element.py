class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        writeIndex=0
        for readIndex in range(len(nums)):
            if nums[readIndex]!=val:
                nums[writeIndex]=nums[readIndex]
                writeIndex+=1
        return writeIndex

