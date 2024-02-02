# BAD_CODE

# def process_student_d(grades):

#     t = sum(grades)
#     avg = t / len(grades)

#     l = "F"
#     if avg>=90:
#         l = "A"
#     elif avg>=90:
#         l = "B"
#     elif avg>=80:
#         l = "C"
#    elif avg>=60:
#         l = "D"
    
#     passed = True
    
#     for g in grades:
#         if g < 60:
#            passed = False
 
  
#     sdt_data = {
#       "average_grade": avg,
#       "grade_letter": l,
#       "all_grade_pass":passed
#       }

#     return sdt_data
   


# BEST PRACTICES

def process_student_data(grades:List[int])->dict:

    total = sum(grades)
    avg = total/ len(grades)

    letter = "F"
    if avg>=90:
        letter = "A"
    elif avg>=90:
        letter = "B"
    elif avg>=80:
        letter = "C"
    elif avg>=60:
        letter= "D"
    
    passed = True
    
    for grade in grades:
        if grade < 60:
           passed = False
 
  
    student_data = {
      "average_grade": avg,
      "grade_letter": letter,
      "all_grade_pass":passed
      }

    return student_data
   
