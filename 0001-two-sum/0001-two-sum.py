class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}

        for index,val in enumerate(nums):
            if (complement:=target-val) in hash_map:
                return [hash_map[complement],index]
            hash_map[val]=index
        return []
       


        

      
        