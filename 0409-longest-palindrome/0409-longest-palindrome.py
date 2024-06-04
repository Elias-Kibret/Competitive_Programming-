class Solution:
    def longestPalindrome(self, s: str) -> int:
        # count=Counter(s)
        # length=0
        # odd_found=False
        # for freq in count.values():
        #     if freq%2==0:
        #         length+=freq
        #     else:
        #         length+=freq-1
        #         odd_found=True
        # if odd_found:
        #     length+=1
        # return length

        ss = set()
        for letter in s:
            if letter not in ss:
                ss.add(letter)
            else:
                ss.remove(letter)
        if len(ss) != 0:
            return len(s) - len(ss) + 1
        else:
            return len(s)
       
       
       

       
        
