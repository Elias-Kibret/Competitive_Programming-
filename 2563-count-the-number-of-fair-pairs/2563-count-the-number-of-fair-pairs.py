from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        def F(x: int) -> int:  # pairs with sum <= x
            l, r = 0, len(nums) - 1
            count = 0
            while l < r:
                if nums[l] + nums[r] <= x:
                    count += (r - l)
                    l += 1
                else:
                    r -= 1
            return count

        return F(upper) - F(lower - 1)