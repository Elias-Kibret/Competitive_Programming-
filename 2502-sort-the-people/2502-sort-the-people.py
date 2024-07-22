class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mp={}

        for index,val in enumerate(heights):
            mp[val]=names[index]

        sorted_heights=sorted(heights, reverse=True)

        for index, val in enumerate(sorted_heights):
            names[index]=mp[val]
        return names

            
        