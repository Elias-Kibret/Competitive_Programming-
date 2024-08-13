class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]

        for index,val in enumerate(nums1):
            found=False

            for num in nums2:
                if val==num:
                    found=True
                if found and num>val:
                    res.append(num)
                    break
            if index+1!=len(res):
                res.append(-1)
            
            
        return res

            
        