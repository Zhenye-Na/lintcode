public class Solution {
    /**
     * @param nums: an array of Integer
     * @param target: target = nums[index1] + nums[index2]
     * @return: [index1 + 1, index2 + 1] (index1 < index2)
     */
    public int[] twoSum(int[] nums, int target) {
        // write your code here
        if (nums == null || nums.length == 0) return new int[2];
        
        int left = 0, right = nums.length - 1;
        
        while (left < right) {
            
            if (nums[left] + nums[right] == target) {
                return new int[]{left + 1, right + 1};
            } else if (nums[left] + nums[right] > target) {
                right--;
            } else {
                left++;
            }
        }

        return new int[2];
    }
}



public class Solution {
    /**
     * @param nums: an array of Integer
     * @param target: target = nums[index1] + nums[index2]
     * @return: [index1 + 1, index2 + 1] (index1 < index2)
     */
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();

        int length = nums.length;
        for (int i = 0; i < length; i++) {
            if (map.get(nums[i]) != null) {
                int[] result = {map.get(nums[i]) + 1, i + 1};
                return result;
            }
            map.put(target - nums[i], i);
        }

        return new int[2];
    }
}