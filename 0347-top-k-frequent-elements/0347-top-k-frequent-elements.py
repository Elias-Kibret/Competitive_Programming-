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


        # count={}

        # freq=[[] for _ in range(len(nums)+1)]
        
        # for n in nums:
        #     count[n]=1+count.get(n,0)
        # for n,c in count.items():
        #     freq[c].append(n)
        # print(freq)

        # res=[]

        # for i in range(len(freq)-1,0,-1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res)==k:
        #             return res
        # return res





        

        