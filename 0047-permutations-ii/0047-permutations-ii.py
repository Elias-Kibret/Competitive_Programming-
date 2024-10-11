class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result=[]
        ps=[]
        used=[False]*len(nums)
        nums.sort()

        self.backtracking(nums,used,ps,result)
        return result

    def backtracking(self,nums:List[int],used:List[bool],ps:List[int],result:List[int])->None:
        if len(ps)==len(nums):
            result.append(ps.copy())
            return 
        for i in range(len(nums)):
            if not used[i] and (i==0 or nums[i]!=nums[i-1] or used[i-1]==True):
                ps.append(nums[i])
                used[i]=True
                self.backtracking(nums,used,ps,result)
                used[i]=False
                ps.pop()
