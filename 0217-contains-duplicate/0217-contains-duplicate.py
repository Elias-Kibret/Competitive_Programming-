class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set()
        for val in nums:
            if val in s:
                return True
            s.add(val)
        return False
      

      
        
            
        
    
      
       
        
    