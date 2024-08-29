class Solution:
    def maxProduct(self, s: str) -> int:
        n=len(s)

        max_product=0


        def is_palindrome(mask:int)-> bool:
            subsequence=[s[i] for i in range(n) if mask&(1<<i)]

            return subsequence==subsequence[::-1]
        
        palindromic_subseq={}

        for mask in range(1,1<<n):
            if is_palindrome(mask):
                palindromic_subseq[mask]=bin(mask).count('1')
        
        for mask1 in palindromic_subseq:
            for mask2 in palindromic_subseq:
                if mask1 &mask2==0:
                    max_product=max(max_product,palindromic_subseq[mask1]*palindromic_subseq[mask2])
        return max_product