class Solution:
    def sumZero(self, n: int) -> List[int]:
        # check if n is odd 
        # append 0
        '''
        dived n by two 
        the file the have with  random number 
        the file the rest with negation the random numbers

        '''
        result=[]

        if n%2 !=0:
            result.append(0)
        for i in range(1,int(n/2)+1):
            result.append(i)
            result.append(-1*i)
        return result

            



        
        