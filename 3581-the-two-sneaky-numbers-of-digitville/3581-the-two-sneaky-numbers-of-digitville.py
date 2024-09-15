class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s=set()
        result=[]

        for val in nums:
            if val in s:
                result.append(val)
            else:
                s.add(val)
        return result

        