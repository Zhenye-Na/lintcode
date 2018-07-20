public class Solution {
    /*
     * @param nums: an array of integers
     * @return: the number of unique integers
     */
    public int deduplication(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) {
            return 0;
        }
        
        Set<Integer> set = new HashSet<>();
        
        int left = 0, right = nums.length - 1;
        
        while (left < right) {
            if (!set.contains(nums[left])) {
                set.add(nums[left]);
                left++;
            } else {
                while (left < right && set.contains(nums[left])) {
                    swap(nums, left, right);
                    right--;
                }
            }
        }

        if (!set.contains(nums[left])) {
            return set.size() + 1;
        }
        return set.size();

    }


    private void swap(int[] nums, int left, int right) {
        int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
    }

}