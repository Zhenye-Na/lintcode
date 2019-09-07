public class Solution {
    /**
     * @param nums: An integer array
     * @return: The length of LIS (longest increasing subsequence)
     */
    public int longestIncreasingSubsequence(int[] nums) {
        // write your code here

        if (nums == null || nums.length == 0) {
            return 0;
        }

        int[] arr = new int[nums.length];
        Arrays.fill(arr, 1);

        int length = nums.length;
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    arr[i] = Math.max(arr[j] + 1, arr[i]);
                }
            }
        }

        int size = 0;
        for (int idx = 0; idx < length; idx++) {
            if (arr[idx] > size) {
                size = arr[idx];
            }
        }

        return size;
    }

}