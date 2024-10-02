class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # nums.sort()

        return sorted(nums)[len(nums)-k]
        