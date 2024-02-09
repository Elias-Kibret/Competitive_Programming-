# https://leetcode.com/problems/replace-elements-in-an-array/description/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dc = {value: index for index, value in enumerate(nums)}
        for x, y in operations:
            nums[dc[x]]=y
            index=dc[x]
            del dc[x]
            dc[y]=index
        return nums
