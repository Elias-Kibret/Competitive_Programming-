class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        mp=Counter(nums)

        for num in nums:
            if mp[num]==1:
                return num