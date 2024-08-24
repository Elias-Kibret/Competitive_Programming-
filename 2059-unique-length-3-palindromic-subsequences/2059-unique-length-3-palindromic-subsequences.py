class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        value_index=defaultdict(list)

        for index,char in enumerate(s):
            if char not in value_index:
                value_index[char]=[index]
            else:
                value_index[char].append(index)

                
                   

        result=set()

      
        for val in value_index.values():
            if len(val)>=2 and val[-1]-val[0]>1:
                low=val[0]+1
                tempResult=val[0]

                while low<val[-1]:
                    tempResult=s[val[0]]+s[low]+s[val[-1]]
                    if tempResult not in result:
                        result.add(tempResult)
                    low+=1
        return len(result)                      





        