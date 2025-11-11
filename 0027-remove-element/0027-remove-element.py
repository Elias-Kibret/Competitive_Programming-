class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        

        count=0
        indexs=[]
        for  i in range(len(nums)):
            if nums[i]!=val:
                count+=1
                indexs.append(nums[i])
        for i in range(len(indexs)):
            nums[i]=indexs[i]
        return count

    
    

