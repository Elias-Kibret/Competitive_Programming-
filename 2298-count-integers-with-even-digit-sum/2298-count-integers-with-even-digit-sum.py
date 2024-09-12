class Solution:
    def isEven(self,nums:str)->bool:

        print(nums)
        nums=sum(int(x) for x in nums)
        return nums%2==0
        
    def countEven(self, num: int) -> int:

        value=2
        count=0

        while value<=num:
            if self.isEven(str(value)):
                count+=1
            value+=1
        return count



        
        