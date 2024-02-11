# https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pivot_index=nums.index(pivot)
        less_piv=[num for num in nums if num<pivot]
        greater_piv=[num for num in nums if num>pivot]
        equal_piv=[num for num in nums if num==pivot]

        return (less_piv+equal_piv+greater_piv)
        
        
                



        
    



        