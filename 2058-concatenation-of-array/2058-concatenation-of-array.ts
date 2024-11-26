function getConcatenation(nums: number[]): number[] {

    let array_length:number=nums.length

    let concatenated_array:number[]=new Array(2*array_length)
    // for(let index in nums){
    //     // console.log(index)
    //     // concatenated_array[index]=nums[index]
    //     // concatenated_array[index+array_length]=nums[index]
    //    console.log(typeof index)
    //    // String
    // }


     for(let index=0; index<array_length;index++){
        concatenated_array[index]=nums[index] 
        concatenated_array[index+array_length]=nums[index] 
     }
    
    return  concatenated_array;

    
};