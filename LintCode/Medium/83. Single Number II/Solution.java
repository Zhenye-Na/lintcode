public class Solution {
    /**
     * @param A: An integer array
     * @return: An integer
     */
    public int singleNumberII(int[] A) {
        // write your code here
        int result = 0, length = A.length, bit;
        for (int i = 0; i < 32; i++) {
            bit = 0;
            for (int k = 0; k < length; k++) {
                bit += (A[k] >>> i) & 1;
            }
            bit = bit % 3;
            result = result | (bit << i);
        }
        return result;
    }
}




public class Solution {
    /**
     * @param A: An integer array
     * @return: An integer
     */
    public int singleNumberII(int[] A) {
        // write your code here
        int ones = 0, twos = 0;
        for(int i = 0; i < A.length; i++){
            ones = (ones ^ A[i]) & ~twos;
            twos = (twos ^ A[i]) & ~ones;
        }
        return ones;
    }
}
