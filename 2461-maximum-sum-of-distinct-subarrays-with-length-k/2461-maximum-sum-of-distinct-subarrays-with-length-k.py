class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = set()
        windowSum = 0     
        best = 0          
        left = 0

        for right in range(len(nums)):
          
            while nums[right] in window:
                window.remove(nums[left])
                windowSum -= nums[left]   
                left += 1

            # Add current element
            window.add(nums[right])
            windowSum += nums[right]

            # When window size reaches k, check and then slide
            if right - left + 1 == k:
                best = max(best, windowSum)
                window.remove(nums[left])
                windowSum -= nums[left]
                left += 1

        return best
