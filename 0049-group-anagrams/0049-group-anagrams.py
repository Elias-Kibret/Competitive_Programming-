class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map=defaultdict(list)

        for val in strs:
            key="".join(sorted(val))
            if key not in hash_map:
                hash_map[key]=[val]
            else:
                hash_map[key].append(val)
        return hash_map.values()

       


                    
