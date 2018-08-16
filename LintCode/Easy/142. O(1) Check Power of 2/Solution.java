public class Solution {
    /**
     * @param n: An integer
     * @return: True or false
     */
    public boolean checkPowerOf2(int n) {
        // write your code here
        return (n > 0) && ((n & (n - 1)) == 0);
    }
}
