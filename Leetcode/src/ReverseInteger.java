public class ReverseInteger {

//    public static void main(String[] args){
//        System.out.println(reverse(1534236469));
//    }


    public static int reverse(int x) {
        int reverse = 0;
        int high_overflow = Integer.MAX_VALUE % 10;
        int low_overflow = Integer.MIN_VALUE % 10;
        while (x != 0) {
            int digit = x % 10;
            if((reverse > Integer.MAX_VALUE/10 || (reverse == Integer.MAX_VALUE/10 && digit >= high_overflow)) || (reverse < Integer.MIN_VALUE/10 || (reverse == Integer.MIN_VALUE/10 && digit <= low_overflow)))
                return 0;
            if (digit != 0 || reverse != 0)
                reverse = reverse * 10 + digit;
            x /= 10;
        }
        return reverse;
    }

}

