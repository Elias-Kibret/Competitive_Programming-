class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int left=0;
        int right=left+k-1;

        int total=0;
        int count=0;

        for( int i=0;i<k;i++){
            total+=arr[i];
        }

        while (right<arr.length){
            if(left>0){
                total=total-arr[left-1]+arr[right];
            }
            if(total/k>=threshold){
                count++;
            }
            left++;
            right++;
        }
        return count;
    }
}