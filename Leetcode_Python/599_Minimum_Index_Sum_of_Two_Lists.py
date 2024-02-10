# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash_map={value:index for index,value in enumerate(list2)}
        result_map={}
        min_sum=0
        result=[]

        for index,value in enumerate(list1):
            if hash_map.get(value)!=None:
                result_map[value]=index+hash_map[value]
        # print(result_map.keys())      
        if len(hash_map)>0:
            min_sum=min(result_map.values())
        for key in result_map.keys():
            if result_map[key]==min_sum:
                result.append(key)
        return result

                    

        