class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        countTicket=0

        i=0

        while tickets[k]!=0:
            if i<len(tickets) and tickets[i]>0:
                tickets[i]-=1
                countTicket+=1
            i+=1
            if i==len(tickets):
                i=0
        return countTicket
                
    