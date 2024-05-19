class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hash_map={}

        for i in range(len(s)):
            if (s[i] in hash_map and hash_map[s[i]]!=t[i]) or (s[i] not in hash_map and t[i] in hash_map.values()):
                return False
            
            hash_map[s[i]]=t[i]
        print(hash_map)

        return True
