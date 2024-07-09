class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        timeChefAt=0
        waitingTime=0

        for customer in customers:
            arrival, cooking=customer

            if timeChefAt<arrival:
                timeChefAt=arrival
            waitingTime+=timeChefAt+cooking-arrival
            timeChefAt+=cooking
        return waitingTime/len(customers)
        