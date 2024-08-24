class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        first_occurence=[-1]*26
        last_occurence=[-1]*26

        for index,char in enumerate(s):
            idx=ord(char)-ord('a')

            if first_occurence[idx]==-1:
                first_occurence[idx]=index

            last_occurence[idx]=index
        print(first_occurence,last_occurence)
        result=set()
        
        for i in range(26):
        
            print(True)
            if first_occurence[i]!=-1 and last_occurence[i]!=-1 and last_occurence[i]-first_occurence[i]>1:
                middle=set(s[first_occurence[i]+1:last_occurence[i]])
                print(middle)

                for val in middle:
                    result.add(chr(i+ord('a'))+val+chr(i+ord('a')))
        return len(result)

       
