from typing import List
from collections import Counter

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        maxi = float('-inf')
        numCount = Counter(nums)
        s = sum(nums)
        
        for i in nums:
            outlier = s - i
            if outlier / 2 == i and numCount[i] == 1:
                continue
            elif numCount[outlier / 2]:
                maxi = max(maxi, i)
        
        return maxi if maxi != float('-inf') else -1