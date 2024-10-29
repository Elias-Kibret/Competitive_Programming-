class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        st=set(nums)
        nums.sort()
    
        longest=0
        for val in nums:
            cur=val
            lg=0
            while cur in st:
                lg+=1
                cur=cur*cur
            longest=max(longest,lg)
        print(longest)
        return longest if longest>1 else -1
           
           
           
           
            
            
            
        
        
    



       


                

        

        