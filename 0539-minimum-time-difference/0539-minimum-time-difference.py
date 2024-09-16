class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        rebuild=[int(char[:2])*60 + int(char[3:]) for char in timePoints]
        print(rebuild)

        
        max_minutes=60*24
        rebuild.sort()
        mn=max_minutes
        
        
        for i in range(1,len(rebuild)):
            mn=min(mn,rebuild[i]-rebuild[i-1])
        return min(mn,1440-rebuild[-1]+rebuild[0])
        