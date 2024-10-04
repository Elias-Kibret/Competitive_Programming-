class Solution:
    def dividePlayers(self, nums: List[int]) -> int:
    

        nums.sort()
        team=nums[0]+nums[-1]
        print(nums)

        l,r=0,len(nums)-1
        print(team)
        total=0

        while l<r:
            if team!=nums[l]+nums[r]:
                return -1
            total+=nums[l]*nums[r]
            l+=1
            r-=1
        return total
            


        