public class Solution {
    /*
     * @param nums: Given an integers array A
     * @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
     */
    public List<Long> productExcludeItself(List<Integer> nums) {
        // write your code here
        List<Long> result = new ArrayList<>();
        if (nums == null || nums.size() == 0 || nums.size() == 1) {
            result.add( (long) 1);
            return result;
        }

        int[] mask = new int[nums.size()];
        Arrays.fill(mask, 1);

        int size = nums.size();
        for (int index = 0; index < size; index++) {
            mask[index] = 0;
            result.add(calculateProduct(nums, mask));
            mask[index] = 1;
        }
        return result;
    }


    private long calculateProduct(List<Integer> nums, int[] mask) {
        long result = 1;
        for (int i = 0; i < mask.length; i++) {
            if (mask[i] != 0) {
                int mul = nums.get(i);
                result = result * (long) mul;
            }
        }

        return result;

    }
}
