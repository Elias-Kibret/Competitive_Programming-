class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map=Counter(nums1)
        intersection=[]
    

        for val in nums2:
            if val in hash_map:
                intersection.append(val)
                if hash_map[val]==1:
                    del hash_map[val]
                else:
                    hash_map[val]=hash_map[val]-1
        return intersection

            
     
    
        