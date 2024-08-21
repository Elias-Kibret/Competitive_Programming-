class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        

        res=0

        for val in words:
            char_count=Counter(chars)
            not_found_char=False
            for char in val:
                if char not in char_count:
                    not_found_char=True
                else:
                    char_count[char]-=1
                    if char_count[char]==0:
                        del char_count[char]
            if not not_found_char:
                print(val)
                res+=len(val)
        return res

                


        