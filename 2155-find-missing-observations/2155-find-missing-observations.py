class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # roles_total=sum(rolls)
        # total=(len(rolls)+n)*mean
      
        # if total<n or (total-roles_total)>n*6 :
        #     return []
        # res=[]
        # for _ in range(n):
        #     res.append((total-roles_total)//n)
        # modulo=((total-roles_total)%n)
        # index=0
        # while modulo!=0:
        #     res[index]=res[index]+1
        #     modulo-=1
        #     index+=1
        # print(res)

        # return res

        m=len(rolls)
        sumM=sum(rolls)
        total_sum=mean*(n+m)

        missing_sum=total_sum-sumM
        base_value=missing_sum//n
        remainder=missing_sum%n

        if base_value<=0 or base_value>6 or (base_value==6 and remainder>0):
            return []
        result=[base_value]*n

        for i in range(remainder):
            result[i]+=1
        return result
        