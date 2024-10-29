class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set(nums)

        longest=0

        nums.sort()

        for val in nums:
            if val-1 not in st:
                count=0
                while val+count in st:
                    count+=1
                longest=max(longest,count)
          
            
        return longest
        