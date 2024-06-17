class Solution {
    public boolean judgeSquareSum(int c) {
        long max_num=(long)Math.sqrt(c);
        long l=0;
        long r=max_num;
        while(l<=r){
           long ans=l*l +r*r;

           if (ans>(long)c){
            r--;
           }
           else if(ans<(long)c){
            l++;
           }
           else{
            return true;
           }
        }
        return false;
        
    }
}