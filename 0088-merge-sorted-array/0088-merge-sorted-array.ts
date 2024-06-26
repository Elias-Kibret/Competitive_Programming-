/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    let index =nums1.length-1
    n=n-1
    while (n>=0){
        nums1[index--]=nums2[n--]
    }
    nums1=nums1.sort((a,b)=>a-b)

    
};