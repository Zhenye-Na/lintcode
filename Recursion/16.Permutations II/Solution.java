public class Solution {
    /*
     * @param :  A list of integers
     * @return: A list of unique permutations
     */
    public List<List<Integer>> permuteUnique(int[] nums) {
        // write your code here
        List<List<Integer>> results = new ArrayList<>();
        if (nums == null || nums.length == 0) {
            results.add(new ArrayList<Integer>());
            return results;
        }
        Arrays.sort(nums);
        helper(nums, new boolean[nums.length], new ArrayList<Integer>(), results);
        return results;
    }

    private void helper(int[] nums,
                        boolean[] visited,
                        List<Integer> permutation,
                        List<List<Integer>> results) {
        
        // Definition: Recursively find all unique permutations

        // Exit:
        if (permutation.size() == nums.length) {
            results.add(new ArrayList<>(permutation));
            return;
        }

        // Split:
        for (int i = 0; i < nums.length; i++) {

            if (visited[i] || ( i > 0 && nums[i] == nums[i - 1] && !visited[i - 1]) ) {
                continue;
            }

            permutation.add(nums[i]);
            visited[i] = true;
            helper(nums, visited, permutation, results);
            permutation.remove(permutation.size() - 1);
            visited[i] = false;
        }

    }

}