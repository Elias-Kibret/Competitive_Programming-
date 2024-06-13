class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        
        return sum(abs(st-stu) for st,stu in zip(seats,students))
       

        