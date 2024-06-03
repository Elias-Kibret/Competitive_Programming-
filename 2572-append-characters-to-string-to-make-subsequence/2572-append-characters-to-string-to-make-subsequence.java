class Solution {
    public int appendCharacters(String s, String t) {
        int s_left=0,t_left=0;
        int s_length=s.length(),t_length=t.length();

        while (s_left<s_length && t_left<t_length){
            if(s.charAt(s_left)==t.charAt(t_left)){
                t_left++;
            }
            s_left++;
        }
        return t_length-t_left;
        
    }
}