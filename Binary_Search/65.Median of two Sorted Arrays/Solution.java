public class Solution {
    /*
     * @param A: An integer array
     * @param B: An integer array
     * @return: a double whose format is *.5 or *.0
     */
    public double findMedianSortedArrays(int[] A, int[] B) {
        // write your code here
        int total = A.length + B.length;
        if (total % 2 == 0) {
            return (findKth(A, 0, B, 0, total / 2) + findKth(A, 0, B, 0, total / 2 + 1)) / 2.0;
        } else {
            return findKth(A, 0, B, 0, total / 2 + 1);
        }
    }

    private int findKth(int[] A, int indexA, int[] B, int indexB, int k) {

        // A is empty
        if (indexA >= A.length) {
            return B[indexB + k - 1];
        }

        // B is empty
        if (indexB >= B.length) {
            return A[indexA + k - 1];
        }

        if (k == 1) {
            return Math.min(A[indexA], B[indexB]);
        }

        int keyA = Integer.MAX_VALUE;
        int keyB = Integer.MAX_VALUE;

        if (indexA + k / 2 - 1 < A.length) {
            keyA = A[indexA + k / 2 - 1];
        }

        if (indexB + k / 2 - 1 < B.length) {
            keyB = B[indexB + k / 2 - 1];
        }

        if (keyA < keyB) {
            return findKth(A, indexA + k / 2, B, indexB, k - k / 2);
        } else {
            return findKth(A, indexA, B, indexB + k / 2, k - k / 2);
        }

    }

}