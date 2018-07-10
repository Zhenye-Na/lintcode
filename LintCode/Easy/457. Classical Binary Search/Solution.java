public class Solution {
    /*
     * @param nums: An integer array sorted in ascending order
     * @param target: An integer
     * @return: An integer
     */
    public int findPosition(int[] nums, int target) {
        // write your code here
        if (nums == null || nums.length == 0) {
            return -1;
        }

        int start = 0, end = nums.length - 1;

        while (start + 1 < end) {
            int mid = (end - start) / 2 + start;

            if (target == nums[mid]) {
                return mid;
            } else if (target < nums[mid]) {
                end = mid;
            } else {
                start = mid;
            }
        }

        if (target == nums[start]) {
            return start;
        }

        if (target == nums[end]) {
            return end;
        }

        return -1;

    }
}