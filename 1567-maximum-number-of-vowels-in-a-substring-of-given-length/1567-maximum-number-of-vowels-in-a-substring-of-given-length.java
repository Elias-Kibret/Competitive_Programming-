class Solution {
    public int maxVowels(String s, int k) {

        Set <Character> vowels=new HashSet<>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');


        int max_count=0;
        int left=0;
        int current_count=0;

        for(int i=0;i<k;++i){
            if(vowels.contains(s.charAt(i))){
                current_count++;
            }
        }
        max_count=current_count;
        for(int i=k;i<s.length();++i){
            if(vowels.contains(s.charAt(i))){
                current_count++;
            }
            if(vowels.contains(s.charAt(i-k))){
                current_count--;
            }
            max_count=Math.max(max_count,current_count);
        }
        return max_count;
    }
}