class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int index=nums1.length-1;
        n=n-1;
        while(n>=0){
            nums1[index--]=nums2[n--];
        }
        Arrays.sort(nums1);
    }
}