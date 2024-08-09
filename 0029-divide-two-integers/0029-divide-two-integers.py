class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign=-1 if dividend*divisor<0 else 1
        
        res=(sign*dividend//divisor)*sign
        if res>2**31-1:
            return res-1
        if res<-2**31:
            return res+1
        return res
        