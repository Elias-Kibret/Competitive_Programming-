class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx=max(candies)
        res=[]

        for val in candies:
            if val+extraCandies>=mx:
                res.append(True)
            else:
                res.append(False)
        return res
        