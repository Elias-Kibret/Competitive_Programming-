class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        HashMap<Character, Integer> map = new HashMap<>();
        int left=0;
        int max_length=0;

        for (int i=0;i<s.length();i++){
            if(map.containsKey(s.charAt(i)) && left<=map.get(s.charAt(i))){
                left=map.get(s.charAt(i))+1;
            }
            else{
                max_length=Math.max(max_length,i-left+1);
            }
            map.put(s.charAt(i),i);
        }
        return max_length;
    }
}