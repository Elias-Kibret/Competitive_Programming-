class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count,left,total_k=0,0,sum(arr[:k])
        right=left+k-1
        
        while right<len(arr):   
            if left>0:
                total_k=total_k-arr[left-1]+arr[right]
            
            if total_k/k>=threshold:
                count+=1
            left+=1
            right+=1
        return count
    
    
        

       
                
            
            
        return count

        