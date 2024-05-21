class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer,Integer> count=new HashMap<Integer,Integer>();

        for(int num:nums){
           if(count.containsKey(num)){
             count.put(num,count.get(num)+1);
           }
           else{
            count.put(num,1);
           }
        }
        int maximum=1;
        int key=nums[0];
        for(Integer k :count.keySet()){
            if(count.get(k)>=maximum){
                key=k;
                maximum=count.get(key);
            }
        }
    return key;

        
    }
}