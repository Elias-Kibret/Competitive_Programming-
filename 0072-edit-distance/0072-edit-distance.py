class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Input: word1, word2
        # Output: the minimum edit distance between word1 and word2

        m = len(word1)  # Length of word1
        n = len(word2)  # Length of word2

        # Create a 2D array dp of size (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize base cases
        for i in range(m + 1):
            dp[i][0] = i  # Deleting all characters from word1 to match an empty word2

        for j in range(n + 1):
            dp[0][j] = j  # Inserting all characters of word2 to match an empty word1

        # Fill the dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:  # Characters match
                    dp[i][j] = dp[i - 1][j - 1]  # No change needed
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],     # Delete operation
                        dp[i][j - 1],     # Insert operation
                        dp[i - 1][j - 1]  # Replace operation
                    )

        return dp[m][n]  # Return the minimum edit distance

# Example usage
if __name__ == "__main__":
    solution = Solution()
    word1 = "kitten"
    word2 = "sitting"
    print(solution.minDistance(word1, word2))  # Output: 3
