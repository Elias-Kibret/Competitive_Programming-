class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result=self.backtracking([],[],nums,0)
        return result+[]

    def backtracking(self,result,subset,nums,index)->List[List[int]]:
        if index==len(nums):
            result.append(subset.copy())
            return result
        self.backtracking(result,subset,nums,index+1)
        subset.append(nums[index])
        self.backtracking(result,subset,nums,index+1)
        subset.pop(-1)
        return result
        
        
        