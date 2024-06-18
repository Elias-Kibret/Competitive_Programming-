class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        jobs=sorted(zip(difficulty,profit))
        worker.sort()

        max_profit=0
        current_max_profit=0

        i=0

        for w in worker:
            while i<len(jobs) and jobs[i][0]<=w:
                current_max_profit=max(current_max_profit,jobs[i][1])
                i+=1
            max_profit+=current_max_profit
        return max_profit
        