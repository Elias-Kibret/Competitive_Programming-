import java.util.*;

class Solution {
    /**
      In this question I have learned the following things 
      1. how to sort array , use Arrays.sort
      2. how to use List wit the list of list in the integer 
      3. how to skip duplicate of conscutive element , 
      we will use while and check if the per and current element is in different locations
        
     */
    public List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);
    
    List<List<Integer>> result=new ArrayList<>();

    for(int i=0;i<nums.length-2;i++){
        // this skip the first duplicate 
        if(i>0 && nums[i]==nums[i-1]) continue;
        int left=i+1;
        int right=nums.length-1;
        while(left<right){
            int sum=nums[i]+nums[left]+nums[right];
            // the duplicate skiping logic must be in the sum of the  
            if(sum==0){
                result.add(Arrays.asList(nums[i],nums[left],nums[right]));
                left++;
                right--;
                //this skip the second element duplicate
                while(left<right&&nums[left]==nums[left-1]){
                    left++;

                }
                // this skip the thrid element duplicate
                while(left<right&&nums[right]==nums[right+1]){
                    right--;
                }
            }
            else if(sum<0){
                left++;
            }
            else{
                right--;
            }

        }
      
    }
      return result;
    }
}

    