class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []

        if len(digits) == 0:
            return result

        self.mp = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        letterCombination = ""
        self.backtracking(digits, 0, result, letterCombination)
        return result

    def backtracking(self, digits: str, index: int, result: List[str], letterCombination: str) -> None:
        if index == len(digits):
            result.append(letterCombination)
            return

        digit = digits[index]
        letters = self.mp[digit]

        for j in range(len(letters)):
            letterCombination += letters[j]
            self.backtracking(digits, index + 1, result, letterCombination)
            # Backtrack by removing the last character
            letterCombination = letterCombination[:-1]
