if __name__ == '__main__':
    result=[]
    grade=[]
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        result.append([name,score])
        grade.append(score)
    grade=sorted(set(grade))
    m=grade[1]
    name=[]
    for val in result:
        if m==val[1]:
            name.append(val[0])
    name.sort()
    for nm in name:
        print(nm)



# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Example

# The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as