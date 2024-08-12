class Solution {
    public int[] getConcatenation(int[] nums) {

        int [] res=new int[nums.length*2];
        int index=0;
        

        for(int val : nums){
            res[index]=val;
            index++;
        }
        for (int val : nums){
            res[index]=val;
            index++;
        }
        return res;
        
        
    }
}