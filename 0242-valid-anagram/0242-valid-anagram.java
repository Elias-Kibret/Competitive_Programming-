class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()){
            return false;
        }


        int [] count=new int[26];
        for(char c:s.toCharArray()){
            count[c-'a']++;
        }
        for(char c:t.toCharArray()){
            count[c-'a']--;
        }
        for(int i=0;i<26;i++){
            if(count[i]!=0){
              return false;
            }
        }
        return true;
    //     HashMap<Character,Integer> count=new HashMap<>();
    //     char[] strArray = s.toCharArray();
        
    //     for(char c: strArray){
    //         count.put(c, count.getOrDefault(c, 0)+1);
    //     }
    //     strArray = t.toCharArray();

    //     for(char c :strArray){
    //         if(!count.containsKey(c) || count.get(c)==0){
    //             return false;
    //         }
    //         count.put(c,count.get(c)-1);
    //     }
    //     return true;
    // }
    }
}