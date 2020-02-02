import java.util.HashMap;
import java.util.Map;

public class RemoveDuplicates{

    public int removeDuplicates(int[] nums) {
        if (nums.length == 0)
            return 0;
        int length = 0;
        Map<Integer, Integer> dupe_map = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            if (dupe_map.get(nums[i]) == null){
                dupe_map.put(nums[i], 1);
                nums[length] = nums[i];
                length++;
                }
            }
        return length;
    }

}
