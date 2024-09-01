class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n!=len(original):
            return []
        res=[[] for _ in range(m)]
        i=0

        for index, val in  enumerate(original):
            res[i].append(val)
            if len(res[i])==n:
                i+=1
            
        return res
        