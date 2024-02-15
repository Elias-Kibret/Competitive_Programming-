# https://leetcode.com/problems/watering-plants/description/

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps=0
        left_capacity=capacity
        for index,value in enumerate(plants):
            if left_capacity>=value:
                steps+=1
                left_capacity=left_capacity-value

            else:
                steps=2*index+steps+1
                left_capacity=capacity-value     
                
        return steps
        