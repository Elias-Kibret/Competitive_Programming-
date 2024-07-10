class Solution {
    public void rotate(int[] nums, int k) {
        int N = nums.length;
        k = k % N; // Handle cases where k is greater than N

        // Reverse the entire array
        reverse(nums, 0, N - 1);
        // Reverse the first k elements
        reverse(nums, 0, k - 1);
        // Reverse the remaining elements
        reverse(nums, k, N - 1);
    }
    
    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}
