class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count={}
        freq=[[] for _ in range(len(nums)+1)]

        for val in nums:
            if val%2==0:
                count[val]=1+count.get(val,0)
        for key,val in count.items():
            freq[val].append(key)
        if len(count)==0:
            return -1
        index=max(count.values(),default=0)
        return min(freq[index])
        