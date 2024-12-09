from typing import List

class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        n = len(nums)
        even_count = 0  # Counter for the number of subarrays with even product
        last_even_index = -1  # Track the index of the last even number

        for i in range(n):
            if nums[i] % 2 == 0:
                # Update the last even index when an even number is found
                last_even_index = i
            # Add subarrays ending at index `i` that include the last even number
            even_count += (last_even_index + 1)

        return even_count

# Example Test Case

