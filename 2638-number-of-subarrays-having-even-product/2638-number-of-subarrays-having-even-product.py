from typing import List

class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        n = len(nums)
        even_count = 0  
        last_even_index = -1  

        for i in range(n):
            if nums[i] % 2 == 0:
              
                last_even_index = i
       
            even_count += (last_even_index + 1)

        return even_count



