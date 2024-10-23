class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        
        # Create a 2D DP array of size (m+1) x (n+1) initialized with 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the DP table iteratively
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # The bottom-right corner of the DP array contains the answer
        return dp[m][n]
