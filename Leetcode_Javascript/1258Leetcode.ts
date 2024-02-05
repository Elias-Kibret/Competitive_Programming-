

function rearrangeArray(nums: number[]): number[] {
    if(nums.length==0) return nums
    let postive:number[]=[]
    let negative:number[]=[]
    nums.forEach((num:number)=>{
        num>=0?postive.push(num):negative.push(num)
    })
    
    let j=0;
    for(let i=0;i<nums.length;i=i+2){
        nums[i]=postive[j]
        nums[i+1]=negative[j]
        j++;
    }
    return nums
    
};
              // Elias Kibret