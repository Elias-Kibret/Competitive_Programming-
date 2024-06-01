class Solution {
    public int totalFruit(int[] fruits) {
      HashMap<Integer,Integer> fruits_count= new HashMap<Integer,Integer>();

      
      int max_length=0;

      for(int right=0,left=0;right<fruits.length;++right){
        fruits_count.put(fruits[right], fruits_count.getOrDefault(fruits[right], 0) + 1);
        while(fruits_count.size()>2){
            fruits_count.put(fruits[left],fruits_count.get(fruits[left])-1);
            if (fruits_count.get(fruits[left])==0){
                fruits_count.remove(fruits[left],0);
            }
            ++left;

        }
        max_length=Math.max(max_length,right-left+1);

      } 
      return max_length; 
    }
}