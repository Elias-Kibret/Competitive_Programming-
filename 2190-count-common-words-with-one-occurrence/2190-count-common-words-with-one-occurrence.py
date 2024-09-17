class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1_count=Counter(words1)
        words2_count=Counter(words2)

        keys=words1_count.keys()
        count=0

        for val in keys:
            if words1_count[val]==1 and words2_count[val]==1:
                count+=1
        return count
             
    

