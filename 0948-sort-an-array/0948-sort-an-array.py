from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # Base case: if the list has 1 or 0 elements, it's already sorted
        if len(nums) > 1:
            mid = len(nums) // 2  # Find the middle point of the list

            # Split the list into two halves
            nums1 = nums[:mid]
            nums2 = nums[mid:]

            # Recursively sort both halves
            self.sortArray(nums1)
            self.sortArray(nums2)

            # Merge the two sorted halves
            self.merge(nums, nums1, nums2)  # Pass 'nums' to store the merged result

        return nums

    # Merge function to merge two sorted lists into one sorted list
    def merge(self, nums: List[int], nums1: List[int], nums2: List[int]):
        i = j = k = 0

        # Merge the two halves into 'nums'
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                nums[k] = nums1[i]
                i += 1
            else:
                nums[k] = nums2[j]
                j += 1
            k += 1

        # If there are remaining elements in nums1, copy them
        while i < len(nums1):
            nums[k] = nums1[i]
            i += 1
            k += 1

        # If there are remaining elements in nums2, copy them
        while j < len(nums2):
            nums[k] = nums2[j]
            j += 1
            k += 1
