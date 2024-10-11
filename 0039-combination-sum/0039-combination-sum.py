class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        ps=[]

        self.backtrack(candidates,target,0,ps,result)
        return result

    def backtrack(self,candidates,target,index,ps,result):
        if target==0:
            result.append(ps.copy())
        if target<0:
            return 
        for i in range(index,len(candidates)):
            ps.append(candidates[i])
            self.backtrack(candidates,target-candidates[i],i,ps,result)
            ps.pop()

