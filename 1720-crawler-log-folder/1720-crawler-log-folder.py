class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count=0

        for val in logs:
            if count>0 and val=='../':
                count-=1   
            elif val!='./' and val!='../':
                count+=1
        return count

        