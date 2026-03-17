class Solution {
    public int characterReplacement(String s, int k) {
        HashMap<Character,Integer> lookup=new HashMap<>();
        int left=0;
        int maxFreq=0;
        int res=0;

        for(int right=0;right<s.length();right++){
             lookup.put(s.charAt(right),lookup.getOrDefault(s.charAt(right),0)+1);
             maxFreq=Math.max(maxFreq,lookup.get(s.charAt(right)));
             while((right-left+1)-maxFreq>k){
                lookup.put(s.charAt(left),lookup.get(s.charAt(left))-1);
                left++;
             }
             res=Math.max(res,right-left+1);
        }
        return res;
        
    }
}