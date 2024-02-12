# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/


class Solution:
    
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        max_num=max(candies)
        for value in candies:
            result.append(value+extraCandies>= max_num)
        return result