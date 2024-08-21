class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res=""
        l=0
        while l<len(num):
            r=l
            check=""
            while r<len(num) and r<l+3:
                if num[l]==num[r]:
                    check+=num[l]
                r+=1
            if len(check)==3:
                if res=="":
                    res=check
                else:
                    res=max(res,check)
                l=r
            else:
                l+=1

            print(res)
                
        
        return res
        
            

                
            

        return res
        