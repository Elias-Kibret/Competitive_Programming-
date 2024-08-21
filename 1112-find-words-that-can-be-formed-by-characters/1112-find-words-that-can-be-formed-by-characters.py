class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        char_count = Counter(chars)
        
        for word in words:
            temp_count = char_count.copy()
            can_form_word = True
            for char in word:
                if temp_count[char] <= 0:
                    can_form_word = False
                    break
                temp_count[char] -= 1
            
            if can_form_word:
                result += len(word)
        
        return result