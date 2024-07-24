class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        def binary(target):
            l,r=0,len(potions)-1
            print(target)
            while l<=r:
                mid=(l+r)//2
                if target<=potions[mid]:
                    r=mid-1
                else:
                    l=mid+1
            return l
        result=[]

        for val in spells:
            # res=binary(math.ceil(success/val))
            result.append((len(potions)-binary(math.ceil(success/val))))
        return result
        