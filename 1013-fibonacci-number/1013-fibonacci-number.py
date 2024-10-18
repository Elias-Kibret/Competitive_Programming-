class Solution:
    def fib(self, n: int) -> int:

        '''
        Bottom Up 
        TC=O(n)
        SC=O(1)
        '''
        if n<1:
            return 0
        
        prev1=0
        prev2=1

        for i in range(2,n+1):
            prev1,prev2=prev2,(prev1+prev2)
        return prev2


        '''
        '''


        '''
        Bottom up 
        Tabulation
        TC=O(n)
        SC=O(n) -> only the array space

        '''
        dp=[-1]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]






        '''
        Top Down Approach
        Memoizations
        TC=O(n)
        SC=O(n)+O(n)=O(n)
        for space complexity we have a recusion space and array space which are O(n)
        '''

    
    
    
    
    #     self.table=[-1]*(n+1)
    #     return self.recDpFib(n)
        



    # def recDpFib(self,n):
    #     print(self.table)
    #     if self.table[n]<0:
    #         if n==0 or n==1:
    #             self.table[n]=n
    #         else:
    #             self.table[n]=self.recDpFib(n-2)+self.recDpFib(n-1)
        # return self.table[n]

    

        
        

        
            
        



        