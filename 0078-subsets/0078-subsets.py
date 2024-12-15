from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)               # Get the number of elements in nums
        totalSubsets = 1 << n 
        print(totalSubsets)      # Calculate 2^n subsets
        result = []                 # List to store all subsets
        
        for i in range(totalSubsets):  # Iterate from 0 to 2^n - 1
            subset = []             # Temporary list to hold the current subset
            for j in range(n):      # Check each bit position
                if i & (1 << j):    # If the j-th bit in i is set, include nums[j]
                    subset.append(nums[j])
            result.append(subset)   # Add the generated subset to the result
        
        return result

