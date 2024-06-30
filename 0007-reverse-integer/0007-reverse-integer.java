class Solution {
    public int reverse(int x) {
        int sign =x<0?-1:1;
        int num=sign*x;
        long reverse=0;

        
        while(num!=0){
            reverse=reverse*10+num%10;
            num/=10;
            if (reverse > Integer.MAX_VALUE || reverse < Integer.MIN_VALUE) {
                return 0;
            }
        }

        return sign*(int)reverse;
        
    }
}