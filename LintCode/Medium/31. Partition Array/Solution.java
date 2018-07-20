public class Solution {
    /**
     * @param nums: The integer array you should partition
     * @param k: An integer
     * @return: The index after partition
     */
    public int partitionArray(int[] nums, int k) {
        // write your code here
        if (nums == null || nums.length == 0) return 0;
        
        int left = 0, right = nums.length - 1;
        
        while (left < right) {
            
            // find the number which is not supposed to be in the left
            while (left < right && nums[left] < k) {
                left++;
            }
            
            // find the number which is not supposed to be in the right
            while (left < right && nums[right] >= k) {
                right--;
            }
            
            // swap two elements
            if (left < right) {
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
            }
            
        }
        
        if (nums[left] < k) {
            return left + 1;
        }
        
        return left;
        
    }
}