public class Maximum_Subarray {
    class Solution {
        public int maxSubArray(int[] nums) {
            int curr_max = Integer.MIN_VALUE;
            int curr_value = 0;

            for (int i = 0; i < nums.length; i++){
                if (nums[i] > curr_max)
                    curr_max = nums[i];
                if(curr_value + nums[i] > 0){
                    curr_value += nums[i];
                    if (curr_value > curr_max)
                        curr_max = curr_value;
                }else
                    curr_value = 0;

            }
            return curr_max;
        }
    }
}
