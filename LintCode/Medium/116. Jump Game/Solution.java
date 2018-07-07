/**
 *  Dynamic Prgramming
 *  Time Complexity: O(n^2)
 */

public class Solution {
    /**
     * @param A: A list of integers
     * @return: A boolean
     */
    public boolean canJump(int[] A) {
        // write your code here
        
        int n = A.length;
        boolean[] f = new boolean[n];
        
        f[0] = true;
        
        for (int j = 1; j < n; j++) {
            
            // Initialization
            f[j] = false;
            
            for (int i = 0; i < n; i++) {
                
                if (f[i] && i + A[i] >= j) {
                    f[j] = true;
                    break;
                }

            }

        }
        
        return f[n - 1];
    }
}





/**
 *  Greedy Algorithm
 *  Time Complexity: O(n)
 */


