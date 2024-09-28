/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarrayGCD = function(nums, k) {

    let count=0

    for(let i=0;i<nums.length;++i){
        let current_gcd=0;
        for(let j=i;j<nums.length;++j){
            let a=current_gcd;
            let b=nums[j]

            while(b!=0){
                [a,b]=[b,a%b]
            }
            current_gcd=a
            if (current_gcd<k){
                break;
            }
            if(current_gcd==k){
                count++;
            }
        }
    }
    return count;
    
};