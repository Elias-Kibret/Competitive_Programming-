

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        timeChefAt = 0
        waitingTime = 0

        for customer in customers:
            arrival, cookTime = customer
            if timeChefAt < arrival:
                timeChefAt = arrival
            waitingTime += timeChefAt + cookTime - arrival
            timeChefAt += cookTime

        return waitingTime / len(customers)
