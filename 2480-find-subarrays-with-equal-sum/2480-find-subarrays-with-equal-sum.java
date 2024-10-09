class Solution {
   public static boolean findSubarrays(int[] nums) {
        // Step 1: Create a HashSet to store the sums of subarrays of length 2
        HashSet<Integer> sumSet = new HashSet<>();
        
        // Step 2: Iterate through the array and calculate the sum of each consecutive pair
        for (int i = 0; i < nums.length - 1; i++) {
            int sum = nums[i] + nums[i + 1];
            
            // Step 3: Check if the sum already exists in the set
            if (sumSet.contains(sum)) {
                return true;  // Found two subarrays with the same sum
            }
            
            // Step 4: Add the current sum to the set
            sumSet.add(sum);
        }
        
        // Step 5: Return false if no two subarrays with the same sum were found
        return false;
    }
}