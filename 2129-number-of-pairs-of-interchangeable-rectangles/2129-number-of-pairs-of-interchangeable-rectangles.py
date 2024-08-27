class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        res=0

        count={}

        for val in  rectangles:
            ration=val[0]/val[1]
            print(ration)

            if ration in count:
                res+=count[ration]
            count[ration]=1+count.get(ration,0)
       
        return res
        