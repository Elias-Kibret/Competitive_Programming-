# from typing import List

# class Solution:
#     def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
#         # Check if the array is large enough for two subarrays of size k
#         if len(nums) < 2 * k:
#             return False
        
#         for i in range(len(nums) - 2 * k + 1):
#             # Slice the first subarray of size k
#             firstK = self.isStrictlyIncreasing(nums[i:i + k])
#             # Slice the second subarray of size k
#             secondK = self.isStrictlyIncreasing(nums[i + k:i + 2 * k])
            
#             # If both subarrays are strictly increasing, return True
#             if firstK and secondK:
#                 return True
#         return False

#     def isStrictlyIncreasing(self, subList: List[int]) -> bool:
#         # Check if the given list is strictly increasing
#         for i in range(1, len(subList)):
#             if subList[i - 1] >= subList[i]:
#                 return False
#         return True
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for a in range(len(nums)-(2*k)+1):
            first_start = a
            b = a+k

            firstArrayIncreasing = True
            for da in range(k - 1):
                # Correct condition to check if NOT increasing
                if nums[first_start + da] >= nums[first_start + da + 1]:
                    firstArrayIncreasing = False
                    break

            if firstArrayIncreasing:
                secondArrayIncreasing = True
                for da in range(k - 1):
                    # Correct condition to check if NOT increasing
                    if nums[b + da] >= nums[b + da + 1]:
                        secondArrayIncreasing = False
                        break
                        
                if secondArrayIncreasing: 
                    return True
			
        return False