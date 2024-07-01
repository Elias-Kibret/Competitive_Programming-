class Solution {
    public int strStr(String haystack, String needle) {
    
        int lenH = haystack.length(),lenN = needle.length();

        
        if (lenN > lenH) {
            return -1;
        }

       
        for (int i = 0; i <= lenH - lenN; i++) {
        
            int j = 0;
            while (j < lenN && haystack.charAt(i + j) == needle.charAt(j)) {
                j++;
            }
            if (j == lenN) {
                return i; 
            }
        }

        
        return -1;

        
    }
}