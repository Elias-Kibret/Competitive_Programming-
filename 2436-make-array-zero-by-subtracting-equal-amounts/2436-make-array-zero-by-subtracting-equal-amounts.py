class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        result=set(nums)

        if 0 not in result:
            return len(result)
        return len(result)-1
        