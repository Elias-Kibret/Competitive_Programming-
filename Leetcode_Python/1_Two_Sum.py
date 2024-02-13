# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:       
        my_dict={}
        for index,value in enumerate(nums):
            comp=target-value
            if comp in my_dict:
                return [index,my_dict[comp]]
            my_dict[value]=index
        return []
                            
