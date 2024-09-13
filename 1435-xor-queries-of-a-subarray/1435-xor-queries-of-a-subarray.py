class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res=[]
        prefixes=[0]

        for item in arr:
            prefixes.append(prefixes[-1]^item)
        for x,y in queries:
            res.append(prefixes[y+1]^prefixes[x])
        print(prefixes)
        print(res)
        return res
       
      
        