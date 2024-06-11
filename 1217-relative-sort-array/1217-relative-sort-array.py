class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        arr1_map=Counter(arr1)
        index=0
        df=[]
        for num in arr1:
            if num not in arr2:
                df.append(num)
        

        for num in arr2:
            for i in range(arr1_map[num]):
                arr1[index]=num
                index+=1
        df.sort()
        index=len(arr1)-1
        for i in range(len(df)-1,-1,-1):
            arr1[index]=df[i]
            index-=1
        return arr1

        

        

    