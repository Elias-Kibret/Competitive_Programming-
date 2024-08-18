class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        hash_map={
            'b':0,
            "a":0,
            "l":0,
            "o":0,
            "n":0
        }
        for val in text:
            if val in hash_map:
                hash_map[val]+=1
        
        res=min(hash_map['l']//2,hash_map['o']//2,min(hash_map.values()))
        


        
        return res
       
        
        

        