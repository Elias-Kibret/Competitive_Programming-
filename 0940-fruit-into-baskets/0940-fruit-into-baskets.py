class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # whenever you have a count hashmap

        count=defaultdict(int)

        l,total,res=0,0,0

        for r in range(len(fruits)):
            count[fruits[r]]+=1
            total+=1

            while len(count)>2:
                f=fruits[l]
                count[f]-=1
                total-=1
                l+=1
                if not count[f]:
                    count.pop(f)
            res=max(res,total)
        return res
        







        # left,right,max_length=0,0,0

        # my_dict={}

        # while right<len(fruits) and left<=right:
        #     while len(my_dict)>2:
        #         my_dict[fruits[left]]=my_dict[fruits[left]]-1
        #         if my_dict[fruits[left]]==0:
        #             del my_dict[fruits[left]]
        #         left+=1
                
        #     if fruits[right] not in my_dict:
        #         my_dict[right]=1
        #     else:
        #         my_dict[fruits[right]]+=1

        #     if len(my_dict)<=2:
        
        #         right+=1            
           
        #     max_length=max(max_length,right-left) 
            
        
            
    


    
                
        # return max_length
        