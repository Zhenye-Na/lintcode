public class Solution {
    /*
     * @param nums: An ineger array
     * @return: An integer
     */
    public int removeDuplicates(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) {
            return 0;
        }

        int start = 0, end = nums.length;
        for (int i = 0; i < end; i++) {
            if (nums[i] != nums[start]) {
                nums[++start] = nums[i];
            }
        }
        return start + 1;
    }
}
