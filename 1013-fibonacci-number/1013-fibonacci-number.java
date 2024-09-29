class Solution {
    public int fib(int n) {
        // if(n==0 || n==1){
        //     return n;
        // }
        // return fib(n-1)+fib(n-2);

        if(n==0 || n==1){
            return n;
        }
        int prev=0;
        int cur=1;

        for(int i=2;i<=n ;i++){
            int temp=prev+cur;
            prev=cur;
            cur=temp;
        }
        return cur;
        
    }
}