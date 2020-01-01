public class Solution {
    /**
     * @param a: An integer
     * @param b: An integer
     * @return: The sum of a and b 
     */
    public int aplusb(int a, int b) {
        // write your code here
        int result = a ^ b;         // + without carry 0+0=0, 0+1=1+0=1, 1+1=0
        int carry = (a & b) << 1;   // 1 + 1 = 2
        if (carry != 0) {
            return aplusb(result, carry);
        }
        return result;
    }
}