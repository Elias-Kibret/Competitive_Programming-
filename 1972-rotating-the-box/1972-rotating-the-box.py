class Solution:
    def solve(self, s):
        """
        Simulates gravity in a single row of the box.
        Stones (#) fall to the rightmost available position (tracked by 'r'),
        stopping at obstacles (*) or the end of the row.
        """
        l, r = len(s) - 1, len(s) - 1  # Initialize pointers at the end of the row
        while l >= 0:
            if s[l] == '.':  # Empty cell
                l -= 1
            elif s[l] == '#':  # Stone
                if s[r] == '.':  # Swap with the rightmost empty position
                    s[l], s[r] = s[r], s[l]
                r -= 1  # Move the empty pointer left
                l -= 1  # Move the current pointer left
            elif s[l] == '*':  # Obstacle
                l -= 1  # Move past the obstacle
                r = l  # Reset the empty pointer to just before the obstacle

    def rotateTheBox(self, box):
        """
        Rotates the box 90 degrees clockwise after simulating gravity.
        """
        # Step 1: Apply gravity to each row
        for row in box:
            self.solve(row)

        # Step 2: Rotate the box
        m, n = len(box), len(box[0])  # Dimensions of the box
        ans = [[None] * m for _ in range(n)]  # Create a new matrix for the rotated box

        for row in range(m):
            for col in range(n):
                ans[col][m - row - 1] = box[row][col]  # Map old coordinates to new

        return ans
