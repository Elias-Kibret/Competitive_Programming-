class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7

        countSubString = 0
        i = 0
        countOnes = 0

        while i < len(s):
            # Count a block of consecutive '1's
            while i < len(s) and s[i] == '1':
                countOnes += 1
                i += 1

            if countOnes > 0:
                # Add contribution of this block, and take modulo
                countSubString = (countSubString + countOnes * (countOnes + 1) // 2) % MOD
                countOnes = 0

            i += 1  # move past '0' (or just overshoot at the end, which is fine)

        return countSubString % MOD
