# https://leetcode.com/problems/relative-ranks
# I sorted the array , to know the exact rank for every scores and store them inside hash map 
# NB I sorted the array not sort...
#  There is a difference between sorted and sort in python

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        nums=sorted(score, reverse=True)
        # sorted in reverse order , so I can get easy the rank of each athlete
        


        dicts={}
        result=[]

        for index,num in enumerate(nums):
            if index==0:
                dicts[num]="Gold Medal"
            elif index==1:
                dicts[num]="Silver Medal"
            elif index==2:
                dicts[num]='Bronze Medal'
            else:
                dicts[num]=str(index+1)
        for s in score:
            result.append(dicts[s])
        return result

        