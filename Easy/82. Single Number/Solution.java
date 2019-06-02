public class Solution {
    /**
     * @param A: An integer array
     * @return: An integer
     */
    public int singleNumber(int[] A) {
        // write your code here
        int result = 0, n = A.length;
        for (int i = 0; i < n; i++) {
            result ^= A[i];
        }
        return result;
    }
}
