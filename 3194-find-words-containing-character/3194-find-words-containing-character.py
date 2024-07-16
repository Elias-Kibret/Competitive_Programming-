class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:

        res=[]
        
        for index,val in enumerate(words):
            if x in val :
                res.append(index)
        return res
