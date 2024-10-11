class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        partialSol=[]
        self.backtrack(nums,0,partialSol,result)
        return result
    def backtrack(self,nums,index,partialSol,result)->None:
        result.append(partialSol.copy())

        for i in range(index,len(nums)):
            partialSol.append(nums[i])
            self.backtrack(nums,i+1,partialSol,result)
            partialSol.pop()


        