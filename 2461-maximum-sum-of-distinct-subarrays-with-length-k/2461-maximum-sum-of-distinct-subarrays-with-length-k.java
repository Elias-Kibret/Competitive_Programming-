class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        
        Set<Integer> window=new HashSet<>();
        long windowSum=0;
        long  subSub=0;
        int left=0;

        for(int right=0;right<nums.length;right++){
            while(window.contains(nums[right])){
                window.remove(nums[left]);
                windowSum-=nums[left++];
            
            }
            windowSum+=nums[right];
            window.add(nums[right]);
            if (right-left+1==k){
                subSub=Math.max(subSub,windowSum);
                window.remove(nums[left]);
                windowSum-=nums[left];
                left++;

            }
        }
        return subSub;
    }

}