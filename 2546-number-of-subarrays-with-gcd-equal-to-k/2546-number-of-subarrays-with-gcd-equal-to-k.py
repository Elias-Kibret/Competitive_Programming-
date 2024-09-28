class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count=0

        for i in range(len(nums)):
            current_gcd=0

            for j in range(i,len(nums)):

                a=current_gcd
                b=nums[j]

                while b!=0:
                    a,b=b,a%b
                current_gcd=a

                if current_gcd<k:
                    break
                if current_gcd==k:
                    count+=1
        return count


        # for i in range(len(nums)-1):
        #     if nums[i]==k:
        #         count+=1
        #     a=nums[i]
        #     b=nums[i+1]

        #     while b!=0:
        #         a,b=b,a%b
        #     if a==k:
        #         print(i)
        #         count+=1
        # if nums[-1]==k:
        #     count+=1
        # return count
        