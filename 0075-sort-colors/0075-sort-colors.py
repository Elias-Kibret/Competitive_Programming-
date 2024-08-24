class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """


    # Brutal Force
        # map_counter=Counter(nums)
        # j=0
        # for i in range(3):
        #     while map_counter[i]!=0:
        #         nums[j]=i
        #         map_counter[i]-=1
        #         j+=1



 
    #  Optimazed way

        low,mid,high=0,0,len(nums)-1


        while mid<=high:
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                mid+=1
                low+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
            

        



       

                