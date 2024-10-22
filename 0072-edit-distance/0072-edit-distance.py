class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Create a memoization table
        memo = {}
        return self.editDistance(word1, word2, len(word1), len(word2), memo)

    def editDistance(self, word1: str, word2: str, m: int, n: int, memo: dict) -> int:
        # Check if the result is already in the memoization table
        if (m, n) in memo:
            return memo[(m, n)]

        # Base cases
        if m == 0:
            return n  # If word1 is empty, insert all characters of word2
        if n == 0:
            return m  # If word2 is empty, delete all characters of word1

        # If the last characters are the same, move to the next characters
        if word1[m - 1] == word2[n - 1]:
            memo[(m, n)] = self.editDistance(word1, word2, m - 1, n - 1, memo)
        else:
            # Calculate minimum of three operations: insert, delete, replace
            insert_op = self.editDistance(word1, word2, m, n - 1, memo)  # Insert
            delete_op = self.editDistance(word1, word2, m - 1, n, memo)  # Delete
            replace_op = self.editDistance(word1, word2, m - 1, n - 1, memo)  # Replace

            memo[(m, n)] = 1 + min(insert_op, delete_op, replace_op)

        return memo[(m, n)]

# Example usage
solution = Solution()
word1 = "dinitrophenylhydrazine"
word2 = "benzalphenylhydrazone"
print(solution.minDistance(word1, word2))  # Output will be calculated efficiently
