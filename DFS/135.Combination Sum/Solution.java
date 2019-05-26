public class Solution {
    /**
     * @param candidates: A list of integers
     * @param target: An integer
     * @return: A list of lists of integers
     */
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        // write your code here
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        if (candidates == null || candidates.length == 0) {
            return results;
        }

        // Remove duplicates and sort the array
        int[] nums = removeDuplicateSort(candidates);

        helper(nums, 0, target, new ArrayList<Integer>(), results);
        return results;
    }

    private void helper(int[] nums,
                        int startIndex,
                        int target,
                        List<Integer> combination,
                        List<List<Integer>> results) {
        // Definition: recursively find correct combinations that sum up to target

        // Exit:
        if (target == 0) {
            results.add(new ArrayList<>(combination));
            return;
        }

        // Split:
        int length = nums.length;
        for (int i = startIndex; i < length; i++) {
            if (nums[i] <= target) {
                combination.add(nums[i]);
                helper(nums, i, target - nums[i], combination, results);
                combination.remove(combination.size() - 1);
            }
        }

    }

    // Remove Duplicate && Sorting
    private int[] removeDuplicateSort(int[] candidates) {
        Arrays.sort(candidates);
    
        int index = 0;
        int length = candidates.length;

        for (int i = 0; i < length; i++) {
            if (candidates[i] != candidates[index]) {
              candidates[++index] = candidates[i];
            }
        }

        int[] nums = new int[index + 1];

        for (int i = 0; i < index + 1; i++) {
            nums[i] = candidates[i];
        }

        return nums;
    }

}