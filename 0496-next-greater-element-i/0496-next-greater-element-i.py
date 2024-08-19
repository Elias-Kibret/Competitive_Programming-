class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        index_map={value:index for index,value in enumerate(nums1)}

        res=[-1]*len(nums1)

        stack=[]

        for num in nums2:
            while stack and num>stack[-1]:
                prev_num=stack.pop()
                res[index_map[prev_num]]=num
            if num in index_map:
                stack.append(num)
        return res
       