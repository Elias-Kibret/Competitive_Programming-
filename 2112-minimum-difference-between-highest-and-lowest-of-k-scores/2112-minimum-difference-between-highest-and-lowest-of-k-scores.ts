function minimumDifference(nums: number[], k: number): number {
    nums=nums.sort((a,b)=>a-b)
    
    let left=0,right=left+k-1;

    let min_score=nums[right]-nums[left]
    left++
    right++

    while (right<nums.length){
        if(min_score>nums[right]-nums[left]){
            min_score=nums[right]-nums[left]
        }
        left++
        right++
    }

    

    return min_score
};