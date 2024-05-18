function removeElement(nums: number[], val: number): number {
    let writeIndex:number=0
    for(let i in nums){
        if(nums[i]!=val){
            nums[writeIndex]=nums[i]
            writeIndex++
        }
    }
    return writeIndex
    
};