class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        pointers
        '''

        left,right=0,len(numbers)-1
        result=[]

        while left<right:
            summed=numbers[left]+numbers[right]

            if summed==target:
                result.append(left+1)
                result.append(right+1)
                break
            elif summed>target:
                right-=1
            else:
                left+=1
        return result


        