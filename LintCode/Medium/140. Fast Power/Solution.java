public class Solution {
    /**
     * @param a: A 32bit integer
     * @param b: A 32bit integer
     * @param n: A 32bit integer
     * @return: An integer
     */
    public int fastPower(int a, int b, int n) {
        // write your code here
        long ret = pow(a, b, n);

        return (int) ret;
    }

    // suppose n > 0
    public static long pow(int a, int b, int n) {
        if (a == 0) {
            return 0;
        }

        // The base case.
        if (n == 0) {
            return 1 % b;
        }

        if (n == 1) {
            return a % b;
        }

        long ret = 0;

        // (a * b) % p = (a % p * b % p) % p （3）
        ret = pow(a, b, n / 2);
        ret *= ret;

        // 这一步是为了防止溢出
        ret %= b;

        if (n % 2 == 1) {
            ret *= pow(a, b, 1);
        }

        // 执行取余操作
        ret = ret % b;

        return ret;
    }
};
