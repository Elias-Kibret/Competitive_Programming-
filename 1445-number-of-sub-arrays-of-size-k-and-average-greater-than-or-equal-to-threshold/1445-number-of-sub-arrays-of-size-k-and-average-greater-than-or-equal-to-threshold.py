class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr)<k:
            return 0
        count=0
        total_k=sum(arr[:k])
        if total_k/k>=threshold:
            count+=1


        left=1
        right=left+k-1
        
        while right<len(arr):
            print(total_k)
            total_k=total_k-arr[left-1]+arr[right]
            if total_k/k>=threshold:
                count+=1
            left+=1
            right+=1
        return count
    
    
        

       
                
            
            
        return count

        