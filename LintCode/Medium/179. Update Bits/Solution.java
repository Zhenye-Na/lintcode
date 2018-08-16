public class Solution {
    /**
     * @param n: An integer
     * @param m: An integer
     * @param i: A bit position
     * @param j: A bit position
     * @return: An integer
     */
    public int updateBits(int n, int m, int i, int j) {
        // write your code here

        // Get all 1's
        int ones = ~0;

        // Create mask -> i ~ j is 1, other positions are 0's
        int mask = ~(((ones << (31 - j)) >>> (31 - j + i)) << i);

        // Keep other position the same, reset ith ~ jth in m and copy m to n
        return (mask & n) | (m << i);
    }
}
