class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    #     my_dict={}

    #     for index,value in enumerate(nums):
    #         if value in my_dict and index-my_dict[value]<=k:
    #             return True
    #         else:
    #             my_dict[value]=index
    #     return False
    # def containsNearbyDuplicate(nums, k):
        if k == 0:
            return False
        window = set()
        for i in range(len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])
            if len(window) > k:
                window.remove(nums[i - k])
        return False
    
    
        
    
    
        
            
        
        
            
    





        

            
            
        
        

