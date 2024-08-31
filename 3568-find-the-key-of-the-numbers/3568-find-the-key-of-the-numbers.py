class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        res=""
        

        while len(res)<4:
            res=str(min(num1%10,num2%10,num3%10))+res
            num1=num1//10
            num2=num2//10
            num3=num3//10
       
        return int(res)
        