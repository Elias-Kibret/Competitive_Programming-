class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        arr_sorted=sorted(arr)
        mp={}
        print(arr_sorted)
        count=1
        for index,key in enumerate(arr_sorted):
            if key not in mp:
                mp[key]=count
                count+=1
            

        res=[]

        for num in arr:
            res.append(mp[num])
        return res
        