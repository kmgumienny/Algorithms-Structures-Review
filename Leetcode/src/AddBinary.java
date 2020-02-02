public class AddBinary {
    class Solution {
        public String addBinary(String a, String b) {
            if (a == null || a.length() == 0) return b;
            if (b == null || b.length() == 0) return a;

            StringBuilder sb = new StringBuilder();
            int len_a = a.length() - 1;
            int len_b = b.length() - 1;
            int leftover = 0;

            while (len_a >= 0 || len_b >= 0){
                int result = 0;
                result  += leftover;
                if (len_a >= 0)
                    result += a.charAt(len_a) - '0';
                if (len_b >= 0)
                    result += b.charAt(len_b) - '0';

                sb.append(result%2);
                leftover = result / 2;
                result = 0;
                len_a--;
                len_b--;
            }
            if(leftover > 0)
                sb.append(leftover);

            return sb.reverse().toString();

        }
    }
}
