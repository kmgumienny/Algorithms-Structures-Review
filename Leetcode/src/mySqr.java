public class mySqr {

    class Solution {
        public int mySqrt(int x) {
            int low = 0;
            int high = Integer.MAX_VALUE;

            while (low != high){
                int medium = low + ((high - low)/2);
                if (medium > x/medium){
                    high = medium - 1;
                    continue;
                }
                else{
                    if (medium + 1 > x/(medium+1))
                        return medium;
                    low = medium + 1;
                    continue;
                }
            }

            return low;
        }
    }
}
