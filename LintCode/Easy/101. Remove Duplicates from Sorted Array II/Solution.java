public class Solution {
    /**
     * @param A: a array of integers
     * @return : return an integer
     */
    public int removeDuplicates(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) {
            return 0;
        }

        Map<Integer, Integer> mapping = new TreeMap<>();
        int length = nums.length;
        for (int i = 0; i < length; i++) {
            if (!mapping.containsKey(nums[i])) {
                mapping.put( nums[i], 1 );
            } else {
                mapping.put( nums[i], mapping.get(nums[i]) + 1 );
            }
        }

        int index = 0;
        for (Map.Entry<Integer, Integer> entry : mapping.entrySet()) {
            int occurence = Math.min(2, entry.getValue());
            System.out.println(occurence);
            for (int num = 0; num < occurence; num++ ) {
                nums[index++] = entry.getKey();
            }
        }

        return index;
    }
}
