public class Solution {
    /**
     * @param num: An integer
     * @return: true if num is an ugly number or false
     */
    public boolean isUgly(int num) {
        // write your code here
        if (num == 0) return false;
        if (num == 1) return true;

        int[] factor = new int[]{2, 3, 5};

        for (int i = 0; i < factor.length; i++) {
            while (num % factor[i] == 0) {
                num = num / factor[i];
            }
        }
        return num == 1;
    }
}
