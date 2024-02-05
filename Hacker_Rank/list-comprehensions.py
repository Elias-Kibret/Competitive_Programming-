if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    permutations = []
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                permutations.append([i, j, k])
    
    print( [x for x in permutations if sum(x) !=n])


#     Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.

# Example




# All permutations of  are:
# .

# Print an array of the elements that do not sum to .


# Input Format

# Four integers  and , each on a separate line.

# Constraints

# Print the list in lexicographic increasing o