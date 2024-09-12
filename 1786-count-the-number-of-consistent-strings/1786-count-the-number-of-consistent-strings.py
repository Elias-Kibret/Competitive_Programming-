class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set=set(allowed)
        count=0

        for word in words:
            found=False
            for char in word:
                if char not in allowed_set:
                    found=True
                    break
            if not found:
                count+=1
        return count
                

        