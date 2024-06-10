class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        new_heigth=sorted(heights)

        count=0

        for i in range(len(heights)):
            if new_heigth[i]!=heights[i]:
                count+=1
        return count
        