class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }
        String X=""+x;
        int right=X.length()-1;
        int left=0;
        while (left<=right){
            if(X.charAt(left)!=X.charAt(right)){
                return false;
            }
            left++;
            right--;

        }
        return true;
    
    }
}