# https://leetcode.com/problems/non-decreasing-array/description/


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        is_non_decreasing = False
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                if is_non_decreasing:
                    return False
                is_non_decreasing = True
                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
        return True