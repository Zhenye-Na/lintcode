public class Solution {
    /**
     * @param nums: An integer array
     * @return: The second max number in the array.
     */
    public int secondMax(int[] nums) {
        // write your code here
        if (nums.length == 1) return nums[0];
        
        int max = Integer.MIN_VALUE;
        int secondmax = Integer.MIN_VALUE;
        
        for (int num : nums) {
            if (num > max) {
                secondmax = max;
                max = num;
            } else if (num > secondmax) {
                secondmax = num;
            }
        }

        return secondmax;

    }
}


public class Solution {
    /**
     * @param nums: An integer array
     * @return: The second max number in the array.
     */
    public int secondMax(int[] nums) {
        // write your code here
        if (nums.length == 1) return nums[0];
        
        for (int i = 0; i < nums.length; i++) {
            int min = nums[i];
            int pos = i;
            for (int j = i; j < nums.length; j++) {
                if (min > nums[j]) {
                    min = nums[j];
                    pos = j;
                }
            }
            
            int tmp = nums[i];
            nums[i] = nums[pos];
            nums[pos] = tmp;
            
        }
        
        return nums[nums.length - 2];
    }
}
