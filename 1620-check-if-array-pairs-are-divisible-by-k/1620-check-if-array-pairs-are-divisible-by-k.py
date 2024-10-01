class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        result=[0]*k

        for num in arr:
            result[num%k]+=1
        for r in range(k):
            if r==0:
                if result[r]%2!=0:
                    return False

            else:
                if result[r]!=result[k-r]:
                    return False
        return True
            
    
        