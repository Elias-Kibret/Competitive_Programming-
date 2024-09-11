class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start=bin(start)[2:].zfill(32)
        goal=bin(goal)[2:].zfill(32)

        print(start,goal)
        count=0
        for i in range(len(start)):
            if(start[i]!=goal[i]):
                count+=1
        return count


        