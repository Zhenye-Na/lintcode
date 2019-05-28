/**
 * Created by Zhenye Na on Jun, 2018
 */


// First trial 1510 ms
public class Solution {
    /**
     * @param n: an integer
     * @return: an ineger f(n)
     */
    public int fibonacci(int n) {
        // write your code here
        int[] result = new int[n + 2]; // fib(50) = 12,586,269,025 > max value of signed 32-bit integer (2,147,483,647)

        result[1] = 0;
        result[2] = 1;

        for (int i = 3; i <= n; i += 1) {
            result[i] = result[i - 1] + result[i - 2];
        }

        return result[n];
    }
}


// Second trial 1540 ms
public class Solution {
    /**
     * @param n: an integer
     * @return: an ineger f(n)
     */
    public int fibonacci(int n) {
        // write your code here
        int first = 0;
        int second = 1;

        if (n == 1) {
            return first;
        } else if (n == 2) {
            return second;
        } else {

            for (int i = 1; i < n; i ++) {
                int tmp = second;
                second += first;
                first = tmp;
            }
            
            return first;
        }
    }
}
