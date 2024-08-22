class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        index_map=defaultdict(list)

        for i, val in enumerate(s):
            if val not in index_map:
                index_map[val]=[i]
            else:
                index_map[val].append(i)
        if len(index_map)==1:
            return 0
        mx=-1

        for val in index_map.values():
            if len(val)>1:
                mx_index=val[-1]
                mn_index=val[0]
                mx=max(mx_index-mn_index-1,mx)
        return mx
        