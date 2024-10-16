class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s)==1:
            return s
        count=Counter(s)

        heap=[]
        for key,value in count.items():
            heapq.heappush(heap,(-value,key))
        print(len(heap))
        result=[]
        if len(heap)<2:
            return ""
        while heap:
            
            first_value,first_char=heapq.heappop(heap)
            if len(heap)==0 and -1*first_value>1:
                return ""
            if len(result)>0 and result[-1]==first_char:
                second_value,second_char=heapq.heappop(heap)
                result.append(second_char)
                second_value+=1
                if second_value<0:
                    heapq.heappush(heap,(second_value,second_char))
                heapq.heappush(heap,(first_value,first_char))
            else:
                result.append(first_char)
                first_value+=1
                if first_value<0:
                    heapq.heappush(heap,(first_value,first_char))
        return "".join(result)

                


        