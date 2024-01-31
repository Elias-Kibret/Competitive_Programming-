class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        if n < 1 or n > 10**4:
          raise ValueError("n must be between 1 and 10^4")
        
        result=[]
        for index in range(1,n+1):
            if index%3==0 and index %5==0:
                result.append("FizzBuzz")
            elif index%3==0:
                result.append("Fizz")
            elif index%5==0:
                result.append("Buzz")
            else:
                result.append(f"{index}")
        return result