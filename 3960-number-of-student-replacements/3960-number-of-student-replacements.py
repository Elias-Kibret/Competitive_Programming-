class Solution:
    def totalReplacements(self, ranks: List[int]) -> int:
        if len(ranks)==0:
            return 0
        minRank=ranks[0]
        countReplacement=0

        for i in range(1,len(ranks)):
            if ranks[i]<minRank:
                minRank=ranks[i]
                countReplacement+=1
        return countReplacement
        