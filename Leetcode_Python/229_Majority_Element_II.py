# https://leetcode.com/problems/majority-element-ii/description/


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash_map={}
        result=[]

        for value in nums:
            hash_map[value]=hash_map.get(value,0)+1
        for key in hash_map.keys():
            print(len(nums)//3)
            if hash_map[key]>len(nums)//3:
                result.append(key)
        return result