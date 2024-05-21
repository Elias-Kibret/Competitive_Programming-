class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=int(len(nums)/2)
        count=Counter(nums)
        maximum=1
        
        
        for key in count.keys():
            if count[key]>=maximum:
                maximum=count[key]
                maxKey=key
        return maxKey
                
            
                

        
        