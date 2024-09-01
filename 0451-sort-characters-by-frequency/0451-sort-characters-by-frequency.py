class Solution:
    def frequencySort(self, s: str) -> str:
        count={}
        res=""

        freq= [[] for _ in range(len(s)+1)]

        for val in s:
            count[val]=1+count.get(val,0)
        for key,value in count.items():
            freq[value].append(key)
        for i in range(len(freq)-1,-1,-1):
            if len(freq[i])>0:
                freq[i].sort()
                for val in freq[i]:
                    for _ in range(count[val]):
                        res+=val
        



        return res
    
        