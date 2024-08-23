class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count=Counter(nums)
        if k>len(nums_count):
            return []
        
        sorted_items = sorted(nums_count.items(), key=lambda x: x[1])[len(nums_count)-k:]
        res=[]

        for val in sorted_items:
            res.append(val[0])
        return res

        

        