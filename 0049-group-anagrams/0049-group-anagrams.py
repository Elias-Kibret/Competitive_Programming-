class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for strg in strs:
            sorted_strg="".join(sorted(strg))
            anagram_dict[sorted_strg].append(strg)
        return anagram_dict.values()


                    
