class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        freq=[[] for _ in range(len(nums)+1)]
        res=[]
        for key ,val in count.items():
            freq[val].append(key)
        for i in range(len(freq)):
            freq[i]=sorted(freq[i],reverse=True)
            for val in freq[i]:
                for i in range(count[val]):
                    res.append(val)

                
        
    
        return res
        