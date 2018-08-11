public class Solution {
    /**
     * @param nums: An array of integers
     * @return: An integer
     */
    public int firstMissingPositive(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) return 1;

        int length = nums.length;
        for (int i = 0; i < length; i++) {
            while (nums[i] > 0 && nums[i] <= length && nums[i] != nums[nums[i] - 1]) {
                int tmp = nums[nums[i] - 1];
                nums[nums[i] - 1] = nums[i];
                nums[i] = tmp;
            }
        }

        for (int j = 0; j < length; j++) {
            if (nums[j] != j + 1) {
                return j + 1;
            }
        }
        return length + 1;

    }
}
