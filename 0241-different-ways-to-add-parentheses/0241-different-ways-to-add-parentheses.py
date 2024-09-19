class Solution:
    def diffWaysToCompute(self, expression: str):
        # If the expression is a pure number, return it as an integer
        if expression.isdigit():
            return [int(expression)]
        
        results = []
        
        # Loop through the expression to find operators
        for i, char in enumerate(expression):
            if char in "+-*":
                # Recursively solve the left and right subexpressions
                left_results = self.diffWaysToCompute(expression[:i])
                right_results = self.diffWaysToCompute(expression[i + 1:])
                
                # Combine the results of the left and right expressions based on the current operator
                for left in left_results:
                    for right in right_results:
                        if char == '+':
                            results.append(left + right)
                        elif char == '-':
                            results.append(left - right)
                        elif char == '*':
                            results.append(left * right)
        
        return results

# Example usage:
solution = Solution()
expression = "2*3-4*5"
print(solution.diffWaysToCompute(expression))
