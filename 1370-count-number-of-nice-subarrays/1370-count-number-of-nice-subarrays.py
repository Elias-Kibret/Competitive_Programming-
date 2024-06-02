class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_count=defaultdict(int)
        current_prefix_sum=0
        prefix_count[0]=1
        nice_subarray_count=0

        for num in nums:
            if num%2!=0:
                current_prefix_sum+=1
            if (current_prefix_sum-k) in prefix_count:
                nice_subarray_count+=prefix_count[current_prefix_sum-k]
            prefix_count[current_prefix_sum]+=1
        return nice_subarray_count 