public class Solution {
    /**
     * @param n: a non-negative integer
     * @return: the total number of full staircase rows that can be formed
     */
    public int arrangeCoins(int n) {
        // Write your code here
        
        if (n < 0) return 0;
        if (n == 1) return 1;
        long start = 1, end = n;
        
        // Binary Search
        while (start + 1 < end) {
            
            long mid = (end - start) / 2 + start;
            long summation = sum(1, mid);

            if (summation > n) {
                end = mid;
            } else {
                start = mid;
            }

        }

        if (sum(1, end) > n) {
            return (int) start;
        } else {
            return (int) end;
        }
    }
    
    private long sum(long start, long end) {
        return (start + end) * (end - start + 1) / 2;
    }

}