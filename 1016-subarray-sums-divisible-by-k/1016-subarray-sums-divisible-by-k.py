class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count={0:1}

        prefix_sum=0
        result=0


        for num in nums:
            prefix_sum+=num

            reminder=prefix_sum%k

            if reminder<0:
                reminder+=k
            if reminder in count:
                result+=count[reminder]
                count[reminder]+=1
            else:
                count[reminder]=1
        return result
        