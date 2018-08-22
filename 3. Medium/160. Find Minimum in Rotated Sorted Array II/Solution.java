public class Solution {
    /**
     * @param nums: a rotated sorted array
     * @return: the minimum number in the array
     */
    public int findMin(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) {
            return -1;
        }

        int start = 0, end = nums.length - 1;
        while (start + 1 < end) {
            int mid = (end - start) / 2 + start;

            if (nums[mid] == nums[end]) {
                end--;
            } else if (nums[mid] > nums[end]) {
                start = mid;
            } else {
                end = mid;
            }

        }

        if (nums[start] <= nums[end]) {
            return nums[start];
        } else {
            return nums[end];
        }


    }
}
