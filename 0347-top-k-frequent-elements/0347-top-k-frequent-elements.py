class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums_count=Counter(nums)
        # if k>len(nums_count):
        #     return []
        
        # sorted_items = sorted(nums_count.items(), key=lambda x: x[1])[len(nums_count)-k:]
        # res=[]

        # for val in sorted_items:
        #     res.append(val[0])


        # return res

        
        count={}
        freq=[[] for _ in range(len(nums)+1)]
        


        for num in nums:
            count[num]=1+count.get(num,0)
        for val,index in count.items():
            freq[index].append(val)
        res=[]
    
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
            if len(res)==k:
                return res
        return res



       

       
       
       
       
