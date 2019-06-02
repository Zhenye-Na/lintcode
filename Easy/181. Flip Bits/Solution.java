public class Solution {
    /**
     * @param a: An integer
     * @param b: An integer
     * @return: An integer
     */
    public int bitSwapRequired(int a, int b) {
        // write your code here
        String bit = Integer.toBinaryString(a ^ b);
        int num = 0;
        for (int i = 0; i < bit.length(); i++) {
            num += (bit.charAt(i) - '0');
        }
        return num;
    }
}
