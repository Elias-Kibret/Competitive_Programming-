class Solution:
    def convertToMinutes(self,time:str)->int:
        hour,minutes=time.split(":")
        return int(hour)*60 +int(minutes)


    def findMinDifference(self, timePoints: List[str]) -> int:
        '''
        convert the HH:MM
        to minutes 

        '''

        minutesPoint=[self.convertToMinutes(val) for val in timePoints]

        # rebuild=[int(char[:2])*60 + int(char[3:]) for char in timePoints]
    

        '''
        in one day we have 
        24 hours and 
        and in 1 hour we have 60 minutes

        '''
        max_minutes=60*24

        '''
        we have to sort the minutes
        why we have to sort 
        because the minutes found in 
        consquective manner 
        '''
        minutesPoint.sort()

        '''
        to find minimum of sth 
        we need to make a first 
        pointer maxiuum
        '''
        min_minutes=max_minutes
        
        
        for i in range(1,len(minutesPoint)):
            min_minutes=min(min_minutes,minutesPoint[i]-minutesPoint[i-1])
        return min(min_minutes,max_minutes-minutesPoint[-1]+minutesPoint[0])
        