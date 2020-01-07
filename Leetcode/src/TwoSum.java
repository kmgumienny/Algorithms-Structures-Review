import java.util.HashMap;
import java.util.Map;

public class TwoSum {

    public static void main(String[] args){
        int[] array = new int[]{2,7,11,15};
        int[] ans = (twoSum(array, 9));
        for (int x: ans) {
            System.out.println(x);
        }
    }

    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            int complement = target - nums[i];
            if(map.containsKey(complement)){
                return new int[] {map.get(complement), i};
            }
            else
                map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No sums");
    }
}
