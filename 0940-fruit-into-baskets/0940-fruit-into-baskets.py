class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # whenever you have a count hashmap

        left,max_length=0,0

        fruits_count={}

        for right in range(len(fruits)):
            fruits_count[fruits[right]]=fruits_count.get(fruits[right],0)+1

            while len(fruits_count)>2:
                fruits_count[fruits[left]]-=1
                if fruits_count[fruits[left]]==0:
                    del fruits_count[fruits[left]]
                left+=1
            max_length=max(max_length,right-left+1)
        return max_length


