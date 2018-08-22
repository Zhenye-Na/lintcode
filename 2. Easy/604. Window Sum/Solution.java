public class Solution {
    /**
     * @param nums: a list of integers.
     * @param k: length of window.
     * @return: the sum of the element inside the window at each moving.
     */
    public int[] winSum(int[] nums, int k) {
        // write your code here
        if (nums == null || nums.length < k || k <= 0) return new int[0];
        
        int length = nums.length;
        int[] prefixSum = new int[length + 1];
        int sum = 0;

        // Prefix Sum array
        for (int i = 0; i < length; i++) {
            sum += nums[i];
            prefixSum[i + 1] = sum;
        }
        
        
        int[] result = new int[length - k + 1];
        for (int i = 0; i < length - k + 1; i++) {
            result[i] = prefixSum[i + k] - prefixSum[i];
        }

        return result;
    }
}