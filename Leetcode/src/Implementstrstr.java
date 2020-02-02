public class ImplementStrstr {

    class Solution {
        public int strStr(String haystack, String needle) {
            if(needle.equals(""))
                return 0;
            if(haystack.equals(""))
                return -1;

            char[] hsk = haystack.toCharArray();
            char[] ndl = needle.toCharArray();

            for (int i = 0; i < hsk.length; i++){
                if (hsk.length - i < ndl.length)
                    return -1;
                if (hsk[i] == ndl[0])
                    for(int j = 0; j < ndl.length; j++){
                        if (hsk[i+j] == ndl[j]){
                            if (j == ndl.length-1)
                                return i;
                        }
                        else
                            break;
                    }
            }
            return -1;
        }
    }
}
