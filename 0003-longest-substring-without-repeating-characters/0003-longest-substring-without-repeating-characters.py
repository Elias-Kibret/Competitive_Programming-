class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dicts={}
        max_len=0
        left_ptr=0

        for i,v in enumerate(s):
            if v in dicts and left_ptr<=dicts[v]:
                left_ptr=dicts[v]+1
            else:
                max_len=max(max_len,i-left_ptr+1)
            dicts[v]=i
        return max_len



    