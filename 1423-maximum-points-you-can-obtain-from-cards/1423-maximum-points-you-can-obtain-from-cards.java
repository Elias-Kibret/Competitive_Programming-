class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int totalSum=0;
        int n=cardPoints.length;

        int minSubSum=Integer.MAX_VALUE;

        int windowSum=0;
        int windowLength=n-k;

        for (int card:cardPoints){
            totalSum+=card;
        }

        if(windowLength==0){
            return totalSum;
        }

        int left=0;

        for (int i=0;i<cardPoints.length;i++){
            windowSum+=cardPoints[i];
            if(i-left+1==windowLength){
                minSubSum=Math.min(minSubSum,windowSum);
                windowSum-=cardPoints[left];
                left++;
            }
        }
        return totalSum-minSubSum;
      
    }
}
