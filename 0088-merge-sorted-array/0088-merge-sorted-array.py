class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged_index=len(nums1)-1
        for value in reversed(nums2):
            nums1[merged_index]=value
            merged_index-=1
        nums1.sort()



    


        