public class Solution {
    /**
     * @param nums: Given the candidate numbers
     * @param target: Given the target number
     * @return: All the combinations that sum to target
     */
    public List<List<Integer>> combinationSum2(int[] nums, int target) {
        // write your code here
        List<List<Integer>> results = new ArrayList<>();
        if (nums == null || nums.length == 0) {
            return results;
        }
        
        Arrays.sort(nums);
        helper(nums, 0, target, new ArrayList<>(), results);
        return results;
    }

    
    private void helper(int[] nums,
                        int startIndex,
                        int target,
                        List<Integer> combinations,
                        List<List<Integer>> results) {
        
        // Definition: Recursively find combinations that sum up to target
        
        // Exit:
        if (target == 0) {
            results.add(new ArrayList<>(combinations));
            return;
        }
        
        // Split:
        for (int i = startIndex; i < nums.length; i++) {
            
            if (i != startIndex && nums[i - 1] == nums[i]) {
                continue;
            }
            
            if (nums[i] > target) {
                break;
            }
            
            combinations.add(nums[i]);
            helper(nums, i + 1, target - nums[i], combinations, results);
            combinations.remove(combinations.size() - 1);

        }

    }

}