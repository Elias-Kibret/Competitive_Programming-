class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_dict=defaultdict(list)

        for index,value in enumerate(nums):
            if value not in my_dict:
                my_dict[value]=[index]
            else:
                my_dict[value].append(index)
        print(my_dict.values())

        for num in my_dict.values():
            
            if len(num)>=2:
                for i in range(len(num)-1):
                    if num[i+1]-num[i]<=k:
                        return True            
        return False
            

            
            
        
        

