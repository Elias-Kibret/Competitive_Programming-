class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n<1:
            return []

        '''
        I will have a list 
        which wll hold all the generated parentheses
        '''

        result=[]

        def backtrack(current:str,open:int,close:int)-> None:

            if len(current)==2*n:
                result.append(current)
            if open<n:
                backtrack(current+"(", open+1,close)
            if close<open:
                backtrack(current+")",open, close+1)
        backtrack("",0,0)
        return result
        