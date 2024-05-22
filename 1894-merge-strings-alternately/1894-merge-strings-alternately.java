class Solution {
    public String mergeAlternately(String word1, String word2) {
        int max_length=Math.max(word1.length(),word2.length());

        int index=0;

        String new_word="";

        while(index<max_length){
            if(index<word1.length()){
               new_word+=word1.charAt(index);
            }
            if(index<word2.length()){
                new_word+=word2.charAt(index);
            }
            index++;
        }
        return new_word;

        

    }
}