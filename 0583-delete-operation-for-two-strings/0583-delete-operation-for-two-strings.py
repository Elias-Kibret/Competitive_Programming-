class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Lengths of word1 and word2
        m = len(word1)
        n = len(word2)
        
        # Create a memoization table initialized with -1
        memo = [[-1] * (n + 1) for _ in range(m + 1)]
        
        # Define the recursive helper function
        def helper(i, j):
            # Base cases
            if i == 0:
                return j  # Delete all characters of word2
            if j == 0:
                return i  # Delete all characters of word1
            
            # If already computed, return the memoized result
            if memo[i][j] != -1:
                return memo[i][j]
            
            # If last characters match, no deletion needed
            if word1[i - 1] == word2[j - 1]:
                memo[i][j] = helper(i - 1, j - 1)
            else:
                # Calculate the minimum deletions
                memo[i][j] = 1 + min(helper(i - 1, j), helper(i, j - 1))
            
            return memo[i][j]
        
        # Call the recursive helper function with the full lengths of the words
        return helper(m, n)

# Example usage
solution = Solution()
word1 = "sea"
word2 = "eat"
print(solution.minDistance(word1, word2))  # Output: 2
