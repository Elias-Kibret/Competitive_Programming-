class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        index_map={num:index for index,num in enumerate(nums1)}

        stack=[]


        result=[-1]*len(nums1)


        for num in nums2:

            while stack and num>stack[-1]:
                prev_num=stack.pop()
                result[index_map[prev_num]]=num

            if num in index_map:
                stack.append(num)

        return result
        

       
      

            
        