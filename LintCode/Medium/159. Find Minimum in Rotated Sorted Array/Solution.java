public class Solution {
    /**
     * @param nums: a rotated sorted array
     * @return: the minimum number in the array
     */
    public int findMin(int[] nums) {
        // write your code here
        
        if (nums.length == 0) return -1;
        
        int start = 0, end = nums.length - 1;
        int target = nums[end];
        
        while (start + 1 < end) {
            int mid = (end - start) / 2 + start;
            
            if (nums[mid] < target) {
                end = mid;
            } else {
                start = mid;
            }
        }
        
        if (nums[start] < target) {
            return nums[start];
        } else {
            return nums[end];
        }
        
        
    }
}