class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        lower_pointer = 0
        upper_pointer = len(nums) - 1

        # while lower_pointer < upper_pointer:
        #     middle_pointer = (lower_pointer + upper_pointer) // 2

        #     # If middle element is greater than upper_pointer element, the minimum is to the right
        #     if nums[middle_pointer] > nums[upper_pointer]:
        #         lower_pointer = middle_pointer + 1
        #     # Otherwise, the minimum is to the left (including middle)
        #     else:
        #         upper_pointer = middle_pointer

        # # At the end, lower_pointer == upper_pointer and points to the minimum
        # return nums[lower_pointer]


        '''
          Recursive solution


        '''


        return self.recSolution(lower_pointer,upper_pointer,nums)
    def recSolution(self,lower_pointer:int,upper_pointer:int,nums:List[int])->int:

        if lower_pointer==upper_pointer:
            return nums[lower_pointer]
        middle_pointer = (lower_pointer + upper_pointer) // 2
        if nums[middle_pointer]>nums[upper_pointer]:
            return self.recSolution(middle_pointer+1,upper_pointer,nums)
        else:
            return self.recSolution(lower_pointer,middle_pointer,nums)




        
