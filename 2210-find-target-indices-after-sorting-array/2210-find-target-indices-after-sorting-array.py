class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        count_number_less_target=0
        count_number_of_target=0
        result=[]

        for val in nums:
            if val<target:
                count_number_less_target+=1
            if val==target:
                count_number_of_target+=1
        start_index=count_number_less_target
        for _ in range(count_number_of_target):
            
            result.append(start_index)
            start_index+=1
        return result


        
                
                
        