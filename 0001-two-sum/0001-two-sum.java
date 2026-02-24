class Solution{
    public int [] twoSum(int [] nums, int target){
        Map<Integer,Integer> lookUp=new HashMap<>();

        for (int index=0; index<nums.length;index++){
            int compliment=target-nums[index];

            if(lookUp.containsKey(compliment)){
                return new int[] {index, lookUp.get(compliment)};
            }
            lookUp.put(nums[index], index);
        }
        return new int [] {};
    }
}