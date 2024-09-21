class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        '''
        intialise result list

        '''
        res=[]


        '''
        '''

        cur=1


        '''
        we will loop 
        till the length of
        a res is less than n

        '''

        while len(res)<n:

            '''
            append the current
            then check
            '''
            res.append(cur)

            if cur*10<=n:
                cur*=10
            else:
                while cur==n or cur%10==9:
                    cur=cur//10
                cur+=1
        return res




        #This is my first solution


        res=[]
        count=1
        while len(res)<n:
            curr=count
            index=0
            res.append(count)

            while index<10 and curr<n:
                curr=int(str(count)+str(index))
                if curr<=n:
                    res.append(curr)
                index+=1
            count+=1
        return res


            
        