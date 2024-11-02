class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Steps:
        1. Initialize two pointers:
            - `lower_pointer` at the start of the list
            - `upper_pointer` at the end of the list
            - `middle_pointer` to find the middle index as `(lower_pointer + upper_pointer) // 2`
        
        2. While `lower_pointer` is less than or equal to `upper_pointer`:
            - If `nums[middle_pointer]` is equal to `target`, return `middle_pointer`.
            
            - If the left half (from `lower_pointer` to `middle_pointer`) is sorted:
                - If `target` is within this range, adjust `upper_pointer` to `middle_pointer - 1`.
                - Otherwise, adjust `lower_pointer` to `middle_pointer + 1`.
            
            - If the right half (from `middle_pointer` to `upper_pointer`) is sorted:
                - If `target` is within this range, adjust `lower_pointer` to `middle_pointer + 1`.
                - Otherwise, adjust `upper_pointer` to `middle_pointer - 1`.
        
        3. If the target is not found, return -1.

        
# Comparison of Approaches for Searching in Rotated Sorted Array
# ==============================================================
# This table summarizes the time and space complexity of different methods for 
# searching a target in a rotated sorted array, covering both brute force and 
# optimized approaches in recursive and iterative forms.

# | Approach                     | Time Complexity | Space Complexity | Efficiency                  |
# |------------------------------|-----------------|------------------|-----------------------------|
# | 1. Brute Force - Linearh     | O(n)            | O(1)             | Slow for large arrays       |
# |     Search                   |                 |                  | Iterates through entire     |
# |                              |                 |                  | array to check each element |
# |------------------------------|-----------------|------------------|-----------------------------|
# | 2. Sort + Binary Search      | O(n log n)      | O(n)             | Inefficient due to sort     |
# |                              |                 |                  | Sorts the array then uses   |
# |                              |                 |                  | binary search on the sorted |
# |------------------------------|-----------------|------------------|-----------------------------|
# | 3. Iterative Rotated Binary  | O(log n)        | O(1)             | Most efficient              |
# |                              |                 |                  | Efficient binary search     |
# |                              |                 |                  | using the rotated structure |
# |------------------------------|-----------------|------------------|-----------------------------|
# | 4. Recursive Rotated Binary  | O(log n)        | O(log n)         | Efficient but uses stack    |
# |                              |                 |                  | Uses recursive binary search|
# |                              |                 |                  | which requires stack space  |
# ==============================================================
#
# Iterative Rotated Binary is typically the most efficient solution due to its 
# optimal time complexity of O(log n) and constant space complexity O(1).


    


        '''
        
        lower_pointer = 0
        upper_pointer = len(nums) - 1
        
        while lower_pointer <= upper_pointer:
            middle_pointer = (lower_pointer + upper_pointer) // 2
            
            # Check if middle element is the target
            if nums[middle_pointer] == target:
                return middle_pointer
            
            # Determine if left half is sorted
            if nums[lower_pointer] <= nums[middle_pointer]:
                # Check if target is within the left half
                if nums[lower_pointer] <= target < nums[middle_pointer]:
                    upper_pointer = middle_pointer - 1
                else:
                    lower_pointer = middle_pointer + 1
            else:
                # Right half must be sorted
                if nums[middle_pointer] < target <= nums[upper_pointer]:
                    lower_pointer = middle_pointer + 1
                else:
                    upper_pointer = middle_pointer - 1
        
        return -1
