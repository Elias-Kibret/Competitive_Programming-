class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        // int index=nums1.length-1;
        // while(n>0){
        //     nums1[index--]=nums2[n=n-1];
        // }
        // Arrays.sort(nums1);
        int i=m-1,k=m+n-1,j=n-1;
        while(j>=0){
            if(i>=0 && nums1[i]>nums2[j]){
                nums1[k--]=nums1[i--];
            }
            else{
                nums1[k--]=nums2[j--];
            }
        }
    }
}