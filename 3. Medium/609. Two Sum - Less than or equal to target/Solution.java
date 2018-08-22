public class Solution {
    /**
     * @param nums: an array of integer
     * @param target: an integer
     * @return: an integer
     */
    public int twoSum5(int[] nums, int target) {
        // write your code here
        if (nums == null || nums.length == 0) {
            return 0;
        }

        Arrays.sort(nums);

        int left = 0, right = nums.length - 1, length = nums.length - 1, count = 0;

        while (left < right) {

            while (left < right && nums[left] + nums[right] <= target) {
                count++;
                left++;
            }
            left = 0;
            right--;
        }
        return count;

    }
}