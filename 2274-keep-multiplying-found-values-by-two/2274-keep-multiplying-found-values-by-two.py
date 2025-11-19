class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        values=set()

        for val  in nums:
            values.add(val)
        if original not in values:
            return original
        check=2*original
        while (check in values):
            check=2*check
        return check
