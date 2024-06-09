class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        result=[]
        MOD = 10**9 + 7
        for i in range(len(nums)):
            result.append(nums[i])
            sub=[nums[i]]
            for j in range(i,len(nums)):
                if(j!=i):
                    sub.append(nums[j])
                    result.append(sum(sub))
        result.sort()
        return sum(result[left-1:right])%MOD




        