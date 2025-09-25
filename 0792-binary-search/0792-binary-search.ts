function search(nums: number[], target: number): number {
    let n=nums.length
    let low=0
    let high=n-1
    while(low<=high){
       let mid=Math.floor((low+high)/2)
       console.log(low,mid,high)
        if(nums[mid]==target)return mid
        else if(nums[mid]<target)low=mid+1
        else high=mid-1
    }
    return -1
    
};