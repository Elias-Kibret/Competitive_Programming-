class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        result=[]

        for val in points:
            
            res=sqrt(val[0]*val[0]+val[1]*val[1])
            result.append([val,res])
            
        result.sort(key=lambda x:x[1])
        
        res=[]
        for i in range(k):
            res.append(result[i][0])
        print(res)

        return res
        