class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count=Counter(arr1)

        result=[]

        for num in arr2:
            if num in count:
                result.extend([num]*count[num])
                del count[num]
        rm=sorted(count.elements())
        result.extend(rm)
        return result
      
       

        

        

    