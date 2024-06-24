/**
 Do not return anything, modify nums in-place instead.
 */
function moveZeroes(nums: number[]): void {
    let left:number=0;
    for (let i in nums){
        if(nums[i]!=0){
            let temp:number=nums[left]
            nums[left]=nums[i];
            nums[i]=temp;
            left++;
        }
    }
};