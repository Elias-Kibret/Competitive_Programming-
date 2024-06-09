class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count=0
        pre_sum_map=defaultdict(int)
        pre_sum_map[0]=1
        prefix=0

        for num in nums:
            prefix+=num
            count+=pre_sum_map[prefix-k]
            pre_sum_map[prefix]+=1
        return count
        

     
            


        