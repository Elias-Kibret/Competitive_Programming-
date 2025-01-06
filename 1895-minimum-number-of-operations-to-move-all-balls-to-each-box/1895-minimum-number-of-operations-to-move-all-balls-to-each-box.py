class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        result=[0]*len(boxes)

        for i in range(len(boxes)):
            count=0
            for j in range(len(boxes)):
                if boxes[j]=='1':
                    count+=abs(j-i)
            result[i]=count
        return result
        