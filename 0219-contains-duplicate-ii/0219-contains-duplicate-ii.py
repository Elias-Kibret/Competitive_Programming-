class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map={}


        for index,val in enumerate(nums):
            if val not in hash_map:
                hash_map[val]=index
                continue 
            elif index-hash_map[val]<=k :
                return True
            hash_map[val]=index
        return False
                
        
        