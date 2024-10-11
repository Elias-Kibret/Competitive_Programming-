class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        ps=[]
        used=[False]*len(nums)

        self.backtrack(nums,used,ps,result)
        return result
    def backtrack(self,nums:List[int],used:List[int],ps:List[int],result:List[int])->None:
        if len(ps)==len(nums):
            result.append(ps.copy())
        for i in range(len(nums)):
            if  not used[i]:
                ps.append(nums[i])
                used[i]=True
                self.backtrack(nums,used,ps,result)
                used[i]=False
                ps.pop()
        