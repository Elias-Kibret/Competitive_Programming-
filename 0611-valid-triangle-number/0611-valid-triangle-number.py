class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        '''
        why we sort it 
        why we start from the reverse loop

        
        '''

        nums.sort()
    
        count=0
        '''
        why do we loop the array in reverse order 
        why do we loop till 2 
        '''
        for i in range(len(nums)-1,1,-1):
            left=0
            right=i-1

            while left<right:
                if nums[left]+nums[right]>nums[i]:
                    '''
                    how do this count work like this 

                    '''
                    count+=right-left
                    '''
                    why do we do this 
                    '''
                    right-=1
                else:
                    left+=1
        return count

           

            
        