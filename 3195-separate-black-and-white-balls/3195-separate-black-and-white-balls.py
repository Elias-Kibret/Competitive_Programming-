class Solution:
    def minimumSteps(self, s: str) -> int:
        ones_before_zeros = 0  # Track how many `1`s are seen before `0`s
        steps = 0  # Count the swaps

        # Traverse through the string
        for char in s:
            if char == '1':
                # Count the number of `1`s encountered so far
                ones_before_zeros += 1
            elif char == '0':
                # For each `0`, add to the total number of swaps needed to move the `1`s past it
                steps += ones_before_zeros
        
        return steps
