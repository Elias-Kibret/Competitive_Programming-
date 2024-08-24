class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # len_single=sum(0+x for x in wall[0])
        # if len_single==1:
        #     return len(wall)
        
        # hash_map={
        #         index:0 for index in range(1,len_single)
        # }

        # print(hash_map)
        # for val in wall:
        #     total=0
        #     for n in val:
        #         total+=n
        #         if total in hash_map:
        #             hash_map[total]+=1
        # print(hash_map)
        
        
        # return  len_single-max(hash_map.values())

        # countGap = defaultdict(int)
        countGap={0:0}

        for row in wall:
            total=0
            for val in row[:-1]:
                total+=val
                countGap[total]=1+countGap.get(total,0)
        return len(wall)-max(countGap.values())
        