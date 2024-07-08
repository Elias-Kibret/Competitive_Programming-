class Solution {
    public int romanToInt(String s) {
        
        Map<Character,Integer> romanMap=new HashMap<>();

        romanMap.put('I',1);
        romanMap.put('V',5);
        romanMap.put('X',10);
        romanMap.put('L',50);
        romanMap.put('C',100);
        romanMap.put('D',500);
        romanMap.put('M',1000);

        int i=0;
        int value=0;

        while(i<s.length()){
            if(i+1<s.length() && romanMap.get(s.charAt(i+1))>romanMap.get(s.charAt(i))){
                value+=romanMap.get(s.charAt(i+1))-romanMap.get(s.charAt(i));
                i+=2;
            }
            else{
                value+=romanMap.get(s.charAt(i));
                i++;
            }
        }
        return value;
    }
}