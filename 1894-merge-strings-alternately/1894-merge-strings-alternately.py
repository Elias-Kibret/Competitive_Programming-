class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_length=max(len(word1),len(word2))
        index=0
    
    
        new_word=""

        while index<max_length:
            if index<len(word1):
                new_word+=word1[index]
            if index<len(word2):
                new_word+=word2[index]
            index+=1
        return new_word
        
    
        