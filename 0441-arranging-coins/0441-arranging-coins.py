class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r=0,n

        while l<=r:
            m=(l+r)//2
            curr=m*(m+1)//2

            if curr==n:
                return m
            if curr<n:
                l=m+1
            else:
                r=m-1
        return r

        