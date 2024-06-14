class Solution {

    public int minIncrementForUnique(int[] nums) {

        Arrays.sort(nums);
        
        int l=0;
        int r=l+1;
        int count=0;
       
        while(r<nums.length){
            if(nums[l]==nums[r]) {
                nums[r]=nums[r]+1;
                count++;
            } 
            else if (nums[l]>nums[r]){
                count+=nums[l]-nums[r]+1;
                nums[r]=nums[l]+1;

            }
            r++;
            l++;
        }
        return count;
    }
}