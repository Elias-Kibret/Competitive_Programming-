// function gcd(num1: number,num2: number): number{
//     while(num2!==0){
//         [num1, num2]=[num1, num1 % num2]
//     }
//     return num1;
// }
function gcd(num1: number, num2: number): number {
    while (num2 !== 0) {
        [num1, num2] = [num2, num1 % num2];
    }
    return num1;
}
function lcm(num1:number,num2:number):number{

    return Math.abs(num1*num2)/gcd(num1,num2)
}



function subarrayLCM(nums: number[], k: number): number {

    let count=0

    for(let i=0;i<nums.length;++i){
        let current_lcm=nums[i]

        for(let j=i;j<nums.length;++j){
            current_lcm=lcm(current_lcm,nums[j])
            if(current_lcm>k){
                break
            }
            if(current_lcm===k){
                count++;
            }
        }
    }
    return count
};

