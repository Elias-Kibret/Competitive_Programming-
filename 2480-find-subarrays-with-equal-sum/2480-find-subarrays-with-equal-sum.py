class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        check=set()

        for i in range(len(nums)-1):
            if nums[i]+nums[i+1] in check:
                return True
            check.add(nums[i]+nums[i+1])
        return False

      
        