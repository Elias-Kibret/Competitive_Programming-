from typing import List

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        my_set = set()
        n = len(nums)

        for start in range(n):
            count = 0
            subArray = []
            for end in range(start, n):
                if nums[end] % p == 0:
                    count += 1
                
                if count > k:
                    break
                
                subArray.append(nums[end])
                my_set.add(tuple(subArray))
        
        return len(my_set)
