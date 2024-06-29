class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #I will use Hashmap , Store every value ,
        # The find max for the number , I will iterate through starting from 1 to the maximum
        # the if there is a missing number in hashmap I will return that number
        # else I will return max number plus 1 which is the will be the next postive number
        # one edge I have to make sure that the max number is postive number 
    
        mp=set() 
        for val in nums:
            if val>0:
                mp.add(val)
        missingPositive=1
        while missingPositive in mp:
            missingPositive+=1
        return missingPositive
            
        
 
        