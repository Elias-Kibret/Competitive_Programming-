class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        lower_pointer=0
        upper_pointer=len(nums)-1

        while lower_pointer<=upper_pointer:
            middle_pointer=(lower_pointer+upper_pointer)//2

            if nums[middle_pointer]==target:
                return True
            
            # compare if a value at lower pointer and upper pointer is equal
            # if equal increase right pointer ,

            if nums[lower_pointer]==nums[middle_pointer]:
                lower_pointer+=1
                continue

            if nums[lower_pointer]<=nums[middle_pointer]:

                if nums[lower_pointer]<=target<nums[middle_pointer]:
                    upper_pointer=middle_pointer-1
                else:
                    lower_pointer=middle_pointer+1
            else:
                if nums[middle_pointer]<target<=nums[upper_pointer]:
                    lower_pointer=middle_pointer+1
                else:
                    upper_pointer=middle_pointer-1
        return False


        