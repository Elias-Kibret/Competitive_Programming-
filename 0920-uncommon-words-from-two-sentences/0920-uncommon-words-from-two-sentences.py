class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        result=[]

        s1_map=Counter(s1.split(" "))
        s2_dic=Counter(s2.split(" "))
        s2=set(s2.split(" "))

        for val in s2:
            if val in s1_map:
                del s1_map[val]
                del s2_dic[val]

            
            
        for key,val in s1_map.items():
            if val==1:
                result.append(key)
        for key,val in s2_dic.items():
            if val==1:
                result.append(key)
        return result

       

    

        