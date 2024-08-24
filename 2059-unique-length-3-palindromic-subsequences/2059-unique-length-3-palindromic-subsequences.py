class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first_occurrence = [-1] * 26  # Track the first occurrence of each character
        last_occurrence = [-1] * 26   # Track the last occurrence of each character
        
        # Traverse the string to fill first and last occurrence arrays
        for i, char in enumerate(s):
            idx = ord(char) - ord('a')
            if first_occurrence[idx] == -1:
                first_occurrence[idx] = i  # First time seeing this character
            last_occurrence[idx] = i  # Update the last occurrence for this character
        
        result = set()
        
        # For each character, check the range between its first and last occurrence
        for i in range(26):
            if first_occurrence[i] != -1 and last_occurrence[i] != -1 and last_occurrence[i] - first_occurrence[i] > 1:
                # Get all unique characters between the first and last occurrence
                middle_chars = set(s[first_occurrence[i] + 1:last_occurrence[i]])
                for middle_char in middle_chars:
                    result.add(chr(i + ord('a')) + middle_char + chr(i + ord('a')))
        
        return len(result)
