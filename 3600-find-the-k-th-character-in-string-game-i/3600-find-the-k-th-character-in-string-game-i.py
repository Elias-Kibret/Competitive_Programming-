class Solution:
    def kthCharacter(self, k: int) -> str:
        return self.rec('a',k)
    def rec(self,word:str,k:int) -> str:
        if len(word)>=k:
            return word[k-1]
        temp=""
        for val in word:
            temp+=chr(ord(val)+1)
        word+=temp
        return self.rec(word,k)







        # word="a"
        # while len(word)<k:
        #     temp=""
        #     for val in word:
        #         temp+=chr(ord(val)+1)
        #     word+=temp
          
        # return word[k-1]
        


   
        