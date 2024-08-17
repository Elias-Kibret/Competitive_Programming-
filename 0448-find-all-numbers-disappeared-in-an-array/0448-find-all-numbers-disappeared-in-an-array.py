class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        st=set({x for x in range(1,len(nums)+1)})
        for val in nums:
            if val in st:
                st.remove(val)

            
        return list(st)

        