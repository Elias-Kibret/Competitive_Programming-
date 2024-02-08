# https://www.geeksforgeeks.org/problems/array-subset-of-another-array2317/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

def isSubset( a1, a2, n, m):
    if m>n:
        return "No"
    
    for value in a2:
        if value not in a1:
            return "No"
        a1.remove(value)
    return "Yes"