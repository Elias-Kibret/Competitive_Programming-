class Solution {
    public boolean canArrange(int[] arr, int k) {
        
        int [] count=new int [k];
        
        for (int num: arr){
            int remainder = (num % k + k) % k;
            count[remainder]++;
        }

        for( int i=0;i<k;i++){
            if(i==0){
                if(count[i]%2!=0){
                    return false;
                }
            }
            else{
                if(k-i>=0){

                if(count[i]!=count[k-i]){
                    return false;
                }
                }
            }
        }
        return true;
    }
}