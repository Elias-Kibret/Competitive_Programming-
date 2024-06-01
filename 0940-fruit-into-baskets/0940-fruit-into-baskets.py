class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # whenever you have a count hashmap

        left,max_length=0,0
        count={}

        for right in range(len(fruits)):
            count[fruits[right]]=count.get(fruits[right],0)+1
            
            while len(count)>2:
                count[fruits[left]]-=1
                if count[fruits[left]]==0:
                    del count[fruits[left]]
                left+=1
            max_length=max(max_length,right-left+1)
        return max_length


        
        




