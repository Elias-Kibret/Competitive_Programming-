class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # countTicket=0

        # i=0

        # while tickets[k]!=0:
        #     if i<len(tickets) and tickets[i]>0:
        #         tickets[i]-=1
        #         countTicket+=1
        #     i+=1
        #     if i==len(tickets):
        #         i=0
        # return countTicket

        res=0

        for i in range(len(tickets)):
            if i<=k:
                res+=min(tickets[i],tickets[k])
            else:
                res+=min(tickets[i],tickets[k]-1)
        return res
                
    