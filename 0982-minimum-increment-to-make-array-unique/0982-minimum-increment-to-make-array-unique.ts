function minIncrementForUnique(nums: number[]): number {

    nums.sort((a,b)=>a-b)
    let l=0,r=1,count=0;
    while(r<nums.length){
        if(nums[l]==nums[r]){
            nums[r]=nums[r]+1
            count++;
        }
        else if (nums[l]>nums[r]){
             count+=nums[l]-nums[r]+1
             nums[r]=nums[l]+1
        }
        l+=1
        r+=1
    }
    return count
    
};