class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        prefix_count=defaultdict(int)
        prefix_count[0]=1

        current_count=0

        nice_array=0


        for num in nums:
            if num%2!=0:
                current_count+=1
            if current_count-k in prefix_count:
                nice_array+=prefix_count[current_count-k]
            prefix_count[current_count]+=1
        return nice_array



















        prefix_count=defaultdict(int)
        prefix_count[0]=1

        current_prefix_count=0
        nice_subarray_count=0

        for num in nums:
            if num%2!=0:
                current_prefix_count+=1
            if(current_prefix_count-k) in prefix_count:
                 nice_subarray_count+=prefix_count[current_prefix_count-k]
            prefix_count[current_prefix_count]+=1
        return nice_subarray_count



