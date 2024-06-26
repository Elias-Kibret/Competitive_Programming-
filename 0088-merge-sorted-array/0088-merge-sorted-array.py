class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index=len(nums1)-1
        n=n-1
        while n>=0:
            nums1[index]=nums2[n]
            n-=1
            index-=1
        nums1.sort()

       
       
       
        
        
        
        

    
      
            
            


