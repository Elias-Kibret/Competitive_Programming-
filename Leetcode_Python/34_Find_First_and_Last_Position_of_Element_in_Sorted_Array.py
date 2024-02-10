# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        result=[]
        mid=(left+right)//2
        if 0 <= mid < len(nums):
            if nums[mid]>=target:
                for i in range(mid):
                    if nums[i]==target:
                        result.append(i)
            if nums[mid]<=target:
                for i in range(mid,len(nums)):
                    if nums[i]==target: 
                        result.append(i)     
            
        if len(result)==1:   
            return [result[0],result[0]]
        elif len(result)>1:
            return [min(result),max(result)]
        else:
            return [-1,-1]
                    