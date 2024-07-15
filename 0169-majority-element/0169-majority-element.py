class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        N=len(nums)//2
        count=Counter(nums)

        for n in count.keys():
            if count[n]>N:
                return n
        
        
        
                
            
                

        
        