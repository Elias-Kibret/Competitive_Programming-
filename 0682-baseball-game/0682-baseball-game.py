class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        result=[]


        for op in operations:
            if op=="+" and len(result)>=2:
                
                result.append((int(result[-1])+int(result[-2])))
            elif op=="D" and len(result)>0:
                result.append((int(result[-1])*2))
            elif op=="C" and len(result)>0:
                result.pop()
            else:
                result.append(int(op))
            print(result)
        return sum(result)