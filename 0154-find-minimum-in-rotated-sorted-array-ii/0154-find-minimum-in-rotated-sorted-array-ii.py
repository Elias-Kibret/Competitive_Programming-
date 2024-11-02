from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        lower_pointer = 0
        upper_pointer = len(nums) - 1

        # Continue binary search until the search space is reduced to one element
        while lower_pointer < upper_pointer:
            middle_pointer = (lower_pointer + upper_pointer) // 2
            
            # Case 1: Right side of mid has the minimum
            if nums[middle_pointer] < nums[upper_pointer]:
                upper_pointer = middle_pointer
            
            # Case 2: Left side of mid has the minimum
            elif nums[middle_pointer] > nums[upper_pointer]:
                lower_pointer = middle_pointer + 1
            
            # Case 3: Uncertain due to duplicates, shrink upper_pointer
            else:
                upper_pointer -= 1  # Reduce search space by one when duplicates are equal

        # At the end, lower_pointer == upper_pointer and points to the minimum
        return nums[lower_pointer]
