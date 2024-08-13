class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res=[-1]*len(arr)
        print(res)
        right=len(arr)-2
        mx=arr[-1]
        while right>=0:
            res[right]=mx
            mx=max(mx,arr[right])
            right-=1
        return res

        
       
                


            
                
        