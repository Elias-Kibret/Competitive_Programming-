# https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
       
        #return: True or False
        
        #code here
        A.sort()
        B.sort()
        
        for index,value in enumerate(A):
            if B[index]!=value:
                return False
        return True