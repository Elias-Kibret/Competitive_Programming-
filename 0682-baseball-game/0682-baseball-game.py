class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        result=[]

        for operation in operations:
            match operation:

                case "+":
                    if result:
                         result.append(result[-1]+result[-2])
                   
                case "D":
                    if result:
                        result.append(result[-1]*2)
                    
                case "C":
                    if result:
                        result.pop()
                    
                case _:
                    result.append(int(operation))
        return sum(result)
  



        