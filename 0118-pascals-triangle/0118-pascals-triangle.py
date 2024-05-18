class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return []

        nums = [[1]]
        row_num = 0

        while row_num < numRows - 1:
            num = [None] * (len(nums[row_num]) + 1)
            for i in range(len(nums)):
                num[0] = 1
                num[-1] = 1
                if i != 0 or i != len(nums) - 1:
                    num[i] = nums[row_num][i - 1] + nums[row_num][i]
            nums.append(num)
            row_num += 1
        return nums
