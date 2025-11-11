/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {

    let merged_index=nums1.length-1;

    for(let i=nums2.length-1;i>=0;i--){
        nums1[merged_index]=nums2[i]
        merged_index-=1
    }
    nums1.sort((a,b)=>a-b)



    
};