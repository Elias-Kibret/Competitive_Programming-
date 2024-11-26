class Solution {
    public int[] getConcatenation(int[] nums) {
        int array_length=nums.length;

        int [] concatenated_array=new int [2*array_length];

        for(int index=0;index<array_length;index++){
            concatenated_array[index]=nums[index];
            concatenated_array[index+array_length]=nums[index];
        }
        return concatenated_array;
        
    }
}