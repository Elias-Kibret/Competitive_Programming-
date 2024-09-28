class Solution:
    '''
    This is how to find the
    LCM of two number
    '''
    def LCM(self,a,b):
        return abs(a*b)//math.gcd(a,b)
    def subarrayLCM(self, nums: List[int], k: int) -> int:

        count=0

        for i in range(len(nums)):

            current_lcm=nums[i]

            for j in range(i,len(nums)):

                current_lcm=self.LCM(current_lcm,nums[j])
                # # If the LCM exceeds K, no need to check further 
                # subarrays starting from this index
                if current_lcm>k:
                    break
                if current_lcm==k:
                    count+=1
        return count
        