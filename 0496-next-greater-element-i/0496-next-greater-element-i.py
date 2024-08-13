class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        mp={val:index for index,val in enumerate(nums1)}

        stack=[]
        res=[-1]*len(nums1)

        for val in nums2:
            while stack and val>stack[-1]:
                p=stack.pop()
                res[mp[p]]=val
            if val in mp:
                stack.append(val)
        return res
      

            
        