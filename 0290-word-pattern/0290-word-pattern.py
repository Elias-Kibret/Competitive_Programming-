class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d1={}
        d2={}
        words=s.split(" ")
        if len(words)!=len(pattern):
            return False

        for char, word in zip(pattern,words):
            if char not in d1:
                d1[char]=word
            elif d1[char]!=word:
                return False
            if word not in d2:
                d2[word]=char
            elif d2[word]!=char:
                return False

        return len(d1.keys())==len(d2.values()) and len(d1.values())==len(d2.keys())


        
      
        

        
           

            
        
    
        
       

    


        