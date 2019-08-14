public class Solution {
    /**
     * @param A: a integer sorted array
     * @param B: a integer sorted array
     * @param K: a integer
     * @return: return a pair of index
     */
    public int[] optimalUtilization(int[] A, int[] B, int K) {
        // write your code here
        if (A == null || A.length == 0) {
            return new int[0];
        }
        if (B == null || B.length == 0) {
            return new int[0];
        }

        int indexA = 0;
        int indexB = 0;

        for (int i = 0; i < A.length; i++) {
            int currentSum = A[indexA] + B[indexB];

            for (int j = 0; j < B.length; j++) {
                if (A[i] + B[j] == K) {
                    return new int[] { i, j };
                } else if (A[i] + B[j] < K) {
                    if (A[i] + B[j] > currentSum) {
                        indexA = i;
                        indexB = j;
                        currentSum = A[indexA] + B[indexB];
                    }
                } else { // A[i] + B[J] > K
                    break;
                }
            }
        }

        return new int[] { indexA, indexB };

    }
}