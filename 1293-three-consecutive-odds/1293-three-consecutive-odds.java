class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {
        if(arr.length<3){
            return false;
        }

        for(int i=0;i<=arr.length-3;++i){
            int j=0;
            while(j<3 && arr[j+i]%2!=0){
                j++;
            }
            if(j==3){
                return true;
            }
        }
        return false;
        
    }
}