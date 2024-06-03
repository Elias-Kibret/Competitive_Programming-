class Solution:
    def totalFruit(self, fruits: List[int]) -> int:


        fruits_count={}

        l,max_count=0,0

        for r in range(len(fruits)):
            fruits_count[fruits[r]]=fruits_count.get(fruits[r],0)+1

            while len(fruits_count)>2:
                fruits_count[fruits[l]]-=1
                if fruits_count[fruits[l]]==0:
                    del fruits_count[fruits[l]]
                l+=1
            max_count=max(max_count,r-l+1)
        return max_count




















        fruits_count={}
        l=0 
        

        res=0

        for r in range(len(fruits)):
            fruits_count[fruits[r]]=fruits_count.get(fruits[r],0)+1

            while len(fruits_count)>2:
                fruits_count[fruits[l]]-=1

                if fruits_count[fruits[l]]==0:
                    del fruits_count[fruits[l]]
                l+=1 
            res=max(res,r-l+1)
        return res
    