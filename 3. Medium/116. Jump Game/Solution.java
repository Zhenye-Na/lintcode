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


 public class Solution {
     /**
      * @param A: A list of integers
      * @return: A boolean
      */
     public boolean canJump(int[] A) {
         // write your code here
         int maxStep = 0, length = A.length;
         for (int index = 0; index < length; index++) {
             // Current position in beyond the maxStep, we cannot reach this position from previous jump
             if (index > maxStep) return false;
             // Update maxStep, select maximum of current index plus the jump step at position index and previous maxStep
             maxStep = Math.max(maxStep, index + A[index]);
         }
         return true;
     }
 }
