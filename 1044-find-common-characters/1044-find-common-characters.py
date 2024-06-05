class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        hash_map=[]
        out_put=[]

        for word in words:
            hash_map.append(Counter(word))

        for key,value in hash_map[0].items():
            min_value=value
            is_found=True

            for index in range(1,len(hash_map)):
                if key not in hash_map[index]:
                    is_found=False
                    break
                else:
                    min_value=min(min_value,hash_map[index][key])
            if is_found:
                for _ in range(min_value):
                    out_put.append(key)
            


        return out_put
        
           


       

     
        