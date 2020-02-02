public class SearchInsertPosition {
    class Solution {
        public int searchInsert(int[] nums, int target) {
            int index = 0;

            while (index < nums.length){
                if (nums[index] == target)
                    break;
                else if (nums[index] < target)
                    index++;
                else if (nums[index] > target)
                    break;
            }
            return index;
        }
    }
}
