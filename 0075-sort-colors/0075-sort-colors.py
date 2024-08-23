class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low,mid,high=0,0,len(nums)-1
        map_counter=Counter(nums)

        # while mid<=high:
        #     if nums[mid]==0:
        #         nums[low],nums[mid]=nums[mid],nums[]
        j=0

        for i in range(3):
            while map_counter[i]!=0:
                nums[j]=i
                map_counter[i]-=1
                j+=1

           
        print(nums)

                