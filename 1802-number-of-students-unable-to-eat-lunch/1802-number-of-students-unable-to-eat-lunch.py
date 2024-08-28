class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentZero = 0
        studentOne = 0
        
        # Count the number of students who prefer 0 and 1
        for student in students:
            if student == 0:
                studentZero += 1
            elif student == 1:
                studentOne += 1
        
        # Try to serve each sandwich in the stack
        for sandwich in sandwiches:
            if sandwich == 0:
                if studentZero > 0:
                    studentZero -= 1
                else:
                    return studentZero + studentOne
            elif sandwich == 1:
                if studentOne > 0:
                    studentOne -= 1
                else:
                    return studentZero + studentOne
        
        return 0
