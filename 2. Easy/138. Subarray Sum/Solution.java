public class Solution {
    /**
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number and the index of the last number
     */
    public List<Integer> subarraySum(int[] nums) {
        // write your code here
        List<Integer> result = new ArrayList<>();
        if (nums == null || nums.length == 0) return result;
        
        // prefix sum -> array index
        Map<Integer, Integer> mapping = new HashMap<>();
        
        // first prefix sum = 0;
        mapping.put(0, -1);
        
        int sum = 0;
        int length = nums.length;

        for (int i = 0; i < length; i++) {
            sum += nums[i];
            
            if (mapping.containsKey(sum)) {
                result.add(mapping.get(sum) + 1);
                result.add(i);
                break;
            } else {
                mapping.put(sum, i);
            }
        }
        
        return result;
        
    }
}