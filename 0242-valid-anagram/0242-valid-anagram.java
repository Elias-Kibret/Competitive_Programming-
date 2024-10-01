class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()){
            return false;
        }
        HashMap<Character,Integer> count=new HashMap<>();
        char[] strArray = s.toCharArray();
        
        for(char c: strArray){
            count.put(c, count.getOrDefault(c, 0)+1);
        }
        strArray = t.toCharArray();

        for(char c :strArray){
            if(!count.containsKey(c) || count.get(c)==0){
                return false;
            }
            count.put(c,count.get(c)-1);
        }
        return true;
    }
}