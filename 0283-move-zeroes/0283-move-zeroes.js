/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let l=0;
    for(let i in nums){
        if(nums[i]!=0){
            let temp=nums[l]
            nums[l]=nums[i]
            nums[i]=temp
            l++;
        }
        // if(nums[l]!=0){
        //     l++
        // }
    }
    
};