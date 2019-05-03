public class Solution {
    /**
     * @param nums: The integer array.
     * @param target: Target to find.
     * @return: The first position of target. Position starts from 0.
     */
    public int binarySearch(int[] nums, int target) {
        // write your code here
        if (nums == null || nums.length == 0) {
            return -1;
        }

        int start = 0, end = nums.length - 1;
        // 相邻就退出
        // start = 1, end = 2 就需要退出循环
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;

            if (target == nums[mid]) {
                end = mid;
            } else if (target < nums[mid]) {
                end = mid;
            } else {
                start = mid;
            }
        }

        // Double Check - First Position
        if (target == nums[start]) {
            return start;
        }

        if (target == nums[end]) {
            return end;
        }

        // not found
        return -1;
    }
}