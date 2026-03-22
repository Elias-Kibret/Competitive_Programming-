class Solution {
    public int maxArea(int[] height) {
        int left=0;
        int right=height.length-1;
        int maxWaterContainer=0;
        while(left<right){
            int minHeight=Math.min(height[left],height[right]);
            maxWaterContainer=Math.max(maxWaterContainer,minHeight*(right-left));
            if(height[left]>height[right]){
                right--;
            }
            else{
                left++;
            }
        }
        return maxWaterContainer;
        
    }
}