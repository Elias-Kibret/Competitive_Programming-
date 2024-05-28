class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        # nums.sort(reverse=True)
        
        # my_dict=Counter(nums)
        
        # for i in range(1,len(nums)):
        #     temp=k
        #     index=i
        #     while temp>0 and index<len(nums):
        #         if nums[i-1]-nums[index]<=temp:
        #             my_dict[nums[i-1]]=my_dict[nums[i-1]]+1
        #         temp=k-(nums[i-1]-nums[index])
        #         index+=1
        # return max(my_dict.values())


        nums.sort()

        l,r,res,total=0,0,0,0

        while r<len(nums):
            total+=nums[r]

            while nums[r]*(r-l+1)>total+k:
                total-=nums[l]
                l+=1
            res=max(res,r-l+1)
            r+=1
        return res
    

            

        

        


        