class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        sortedMeeting=sorted(intervals,key=lambda x:x[1])
        print(sortedMeeting)

        for i in range(len(sortedMeeting)-1):

            if sortedMeeting[i][1]>sortedMeeting[i+1][0]:
                return False
        return True


   
                
        
        