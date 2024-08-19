class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=set()
        nums1Set=set(nums1)

        for val in nums2:
            if val in nums1Set:
                res.add(val)
        return list(res)
        