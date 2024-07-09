class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        N = len(customers)
        
        total = 0
        current = 0
        for a, t in customers:
            # if a comes after, then update current
            current = max(a, current)
            total += t + (current - a)
            current += t
        return total / N