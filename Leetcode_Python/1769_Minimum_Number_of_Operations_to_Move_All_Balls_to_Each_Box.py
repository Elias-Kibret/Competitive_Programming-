# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer=[]
        one_ball = [index for index in range(len(boxes)) if boxes[index] == '1']

        for i in range(len(boxes)):
            operations=0
            for j in one_ball:
                operations=operations+abs(j-i)
            answer.append(operations)


        return answer
    
    
        # for i in range(len(boxes)):
        #     operation=0
        #     for j in range(len(boxes)):
                
        #         if boxes[j]=='1':
        #             print(boxes[j])
        #             operation=operation+abs(j-i)

        #     answer.append(operation)
    
        # return answer