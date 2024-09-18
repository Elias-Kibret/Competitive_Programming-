class Solution:
    def smallestNumber(self, num: int) -> int:
        if len(str(num))==1:
            return num
        sign=1
        if num<0:
            num=num*-1
            sign=-1
        
        num=[int(x) for x in str(num) ]
        count_num=Counter(num)
        count_zero=count_num[0]
        del count_num[0]

        num=[]

        for key , val in count_num.items():
            temp=[key]*val
            num+=temp
        
       
        
        num=sorted(num)if sign>0 else sorted(num,reverse=True)
        result=str(num[0])
        
        if sign>0:
            while count_zero>0:
                result+="0"
                count_zero-=1
        for i in range(1,len(num)):
            result+=str(num[i])
        if sign<0:
            while count_zero>0:
                result+=str("0")
                count_zero-=1
        print(result)
        return sign*int (result)


        


        