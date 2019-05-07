public class Solution {
    /*
     * @param nums: A list of integers.
     * @return: A list of permutations.
     */
    public List<List<Integer>> permute(int[] nums) {
        // write your code here
        List<List<Integer>> results = new ArrayList<>();
        if (nums == null || nums.length == 0) {
            results.add(new ArrayList<Integer>());
            return results;
        }
        
        helper(nums, 0, new ArrayList<Integer>(), results);
        return results;
    }


    private void helper(int[] nums,
                        int startIndex,
                        List<Integer> permutation,
                        List<List<Integer>> results) {
        
        // Definition: recursively permutate array

        // Exit:
        if (permutation.size() == nums.length) {
            results.add(new ArrayList<Integer>(permutation));
            return;
        }


        // Split:
        for (int i = startIndex; i < nums.length; i++) {
            if (!permutation.contains(nums[i])) {
                permutation.add(nums[i]);
                // Here startIndex cannot be i + 1, because we cannot get [1, 3, 2] from [1, 2, 3] in this way
                helper(nums, 0, permutation, results);
                permutation.remove(permutation.size() - 1);
            }

        }
        
    }

}
