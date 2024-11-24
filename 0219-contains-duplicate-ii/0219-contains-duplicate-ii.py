class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}  # To store the last index of each element
        
        for index, val in enumerate(nums):
            if val in hash_map and index - hash_map[val] <= k:
                return True  # Found a valid duplicate within the range
            hash_map[val] = index  # Update the last index of the element
        
        return False  # No valid duplicate found
