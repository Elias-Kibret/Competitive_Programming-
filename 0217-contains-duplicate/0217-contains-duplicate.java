class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> lookup=new HashSet<>();

        for(int num: nums){
            if(lookup.contains(num)){
                return true;
            }
            lookup.add(num);
        }
        return false;
    }
}