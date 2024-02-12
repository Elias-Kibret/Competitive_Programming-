# https://leetcode.com/problems/keyboard-row

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        def check(word,row):
            return all(letter in row for letter in word.lower() )

        result=[]

        rows=["qwertyuiop","asdfghjkl","zxcvbnm"]
        
        for word in words:
            for row in rows:
                if check(word,row):
                    result.append(word)
                    break
        return result

        