// Solution 1: 利用HashSet去重，效率低下

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
        
        helper(nums, new boolean[nums.length], new ArrayList<Integer>(), results);
        
        Set<List<Integer>> hs = new HashSet<>();
        hs.addAll(results);
        results.clear();
        results.addAll(hs);
        return results;
    }
    
    private void helper(int[] nums,
                        boolean[] visited,
                        List<Integer> permutation,
                        List<List<Integer>> results) {
        
        // Definition: recursively permutate array

        // Exit:
        if (permutation.size() == nums.length) {
            results.add(new ArrayList<Integer>(permutation));
            return;
        }

        // Split:
        for (int i = 0; i < nums.length; i++) {
            if (!visited[i]) {
                permutation.add(nums[i]);
                visited[i] = true;
                helper(nums, visited, permutation, results);
                permutation.remove(permutation.size() - 1);
                visited[i] = false;
            }

        }
        
    }
}




// Solution 2: Double check

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