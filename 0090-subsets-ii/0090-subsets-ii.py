class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        ps=[]
        nums.sort()

        self.backtrack(nums,0,ps,result)
        return result

    def backtrack(self,nums: List[int],index: int,ps: List[int],result: List[int])->None:
        result.append(ps.copy())

        for i in range(index,len(nums)):
            if i>index and nums[i]==nums[i-1]:
                continue
            ps.append(nums[i])
            self.backtrack(nums,i+1,ps,result)
            ps.pop()
