public class Solution {
    /**
     * @param r: a Integer represent radius
     * @return: the circle's circumference nums[0] and area nums[1]
     */
    public double[] calculate(int r) {
        // write your code here
        return new double[]{3.14 * r * 2, 3.14 * r * r};
    }
}