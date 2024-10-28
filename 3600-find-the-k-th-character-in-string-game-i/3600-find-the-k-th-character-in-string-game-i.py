class Solution:
    def kthCharacter(self, k: int) -> str:
        word="a"
        while len(word)<k:
            temp=""
            for val in word:
                temp+=chr(ord(val)+1)
            word+=temp
            # print(word)
        return word[k-1]
        


    # def rec(self,word,k):
    #     if len
        

    #     if len(s)


    
        