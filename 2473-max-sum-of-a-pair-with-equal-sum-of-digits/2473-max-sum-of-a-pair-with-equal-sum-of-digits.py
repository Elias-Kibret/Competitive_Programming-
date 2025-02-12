class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        mp=defaultdict(list)

     
        
        for num in nums:
            nums_digit_sum=self.sumDigit(num)
            if nums_digit_sum in mp:
                mp[nums_digit_sum].append(num)
            else:
                mp[nums_digit_sum]=[num]
        
        total=-1
        for key, value in mp.items():
            if len(value)>=2:
                value.sort(reverse=True)
                if(value[0]+value[1])>total:
                    total=value[0]+value[1]

                
        return total





    def sumDigit(self,num:str):
        result=0

        for digit in str(num):
            result+=int(digit)
        return result

        