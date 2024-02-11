# https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

# class Solution:
#     def rearrangeArray(self, nums: List[int]) -> List[int]:
#         postive_number=[num for num in nums if num>0 ]
#         negative_number=[num for num in nums if num<0]

#         result=[]
#         for index in range(len(nums)//2):
#             result.append(postive_number[index])
#             result.append(negative_number[index])
#         return result


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = [num for num in nums if num > 0]
        negative = [num for num in nums if num < 0]

        nums[0 : len(nums) : 2] = positive
        nums[1 : len(nums) : 2] = negative

        return nums