class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def getNum(num: int) -> int:
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        while n != 1 and n not in seen:
            seen.add(n)
            n = getNum(n)
        
        return n == 1

