public class Solution {
    /**
     * @param nums: A list of integer which is 0, 1 or 2 
     * @return: nothing
     */
    public void sortColors(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) {
            return;
        }

        int left = 0, right = nums.length - 1, length = nums.length;

        for (int i = 0; i < length; i++) {
            if (nums[i] < 1) {
                swap(nums, left, i);
                left++;
            } else if (nums[i] > 1) {
                swap(nums, right, i);
                i--;
                right--;
            }
        }
    }


    private void swap(int[] nums, int left, int right) {
        int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
    }

}