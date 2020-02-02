public class PlusOne {

    class Solution {
        public int[] plusOne(int[] digits) {
            if (digits.length == 0)
                return new int[]{0};

            for (int i = 0; i < digits.length; i++){
                if (i == digits.length - 1 && digits[i] == 9){
                    int[] newArray = new int[digits.length+1];
                    newArray[0] = 1;
                    return newArray;
                }else if (digits[i] != 9)
                    break;
            }

            boolean carry = true;
            for (int i = digits.length -1; i >= 0; i--){
                if (digits[i] == 9 && carry){
                    digits[i] = 0;
                    carry = true;
                }
                else if (carry){
                    digits[i] += 1;
                    return digits;
                }
            }

            return digits;

        }
    }
}
