public class PalindromeNumber{

//    public static void main(String[] args){
//        boolean answer = isPalindrome(121);
//    }


    public boolean isPalindrome(int x) {
        if (x < 0)
            return false;
        int x_copy = x;
        int backwards = 0, remainder = 0;
        while(x_copy != 0){
            remainder = x_copy % 10;
            backwards = backwards * 10 + remainder;
            x_copy /= 10;
        }
        if (backwards == x)
            return true;
        return false;
    }
}