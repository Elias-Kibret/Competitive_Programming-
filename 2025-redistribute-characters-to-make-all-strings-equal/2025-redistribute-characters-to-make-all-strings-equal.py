class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count={}

        for word in words:
            for c in word:
                count[c]=count.get(c,0)+1
        n=len(words)
        
        for val in count.values():
            if val%n!=0:
                return False
        return True