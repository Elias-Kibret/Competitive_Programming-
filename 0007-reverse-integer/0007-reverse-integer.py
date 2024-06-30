class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        num = sign*x
        reverse = 0
        
        while num != 0:
            reverse = reverse * 10 + num % 10
            num //= 10
        
        reverse *= sign
        
        if reverse > (2**31) - 1 or reverse < -2**31:
            return 0
        
        return reverse
