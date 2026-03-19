class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        int left=0;
        HashSet<Integer> lookUp=new HashSet<>();

        for(int right=0;right<nums.length;right++){
            if(lookUp.size()>k){
                lookUp.remove(nums[left]);
                left++;
            }
            if(lookUp.contains(nums[right]) && lookUp.contains(nums[left]) && lookUp.size()<=k){
                return true;
            }
            lookUp.add(nums[right]);
        }
        return false;
    }
}