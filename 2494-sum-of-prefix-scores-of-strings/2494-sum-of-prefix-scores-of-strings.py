class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        hMap={}
        for word in words:
            s=""
            for char in word:
                s+=char 
                hMap[s]=hMap.get(s,0)+1
        res=[]
        for word in words:
            count=0
            s=""
            for char in word:
                s+=char
                count+=hMap[s]
                
            res.append(count)
        return res
                
        