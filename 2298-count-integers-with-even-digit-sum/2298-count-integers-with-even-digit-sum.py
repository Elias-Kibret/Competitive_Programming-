class Solution:
        
    def countEven(self, num: int) -> int:
        count=0

        for n in range(2,num+1):
            digits, total=n,0

            while digits:
                digits,digit=divmod(digits,10)
                total+=digit
            if total%2==0:
                count+=1
        return count




    #     value=2
    #     count=0

    #     while value<=num:
    #         if self.isEven(str(value)):
    #             count+=1
    #         value+=1
    #     return count

    # def isEven(self,nums:str)->bool:

    #     print(nums)
    #     nums=sum(int(x) for x in nums)
    #     return nums%2==0


        
        