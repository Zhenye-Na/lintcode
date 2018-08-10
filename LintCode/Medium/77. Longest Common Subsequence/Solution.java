public class Solution {
    /**
     * @param A: A string
     * @param B: A string
     * @return: The length of longest common subsequence of A and B
     */
    public int longestCommonSubsequence(String A, String B) {
        // write your code here
        if (A == null || B == null || A.length() == 0 || B.length() == 0) {
            return 0;
        }

        int lengthA = A.length();
        int lengthB = B.length();

        int[][] arr = new int[lengthB + 1][lengthA + 1];
        for (int j = 1; j <= lengthB; j++) {
            for (int i = 1; i <= lengthA; i++) {
                if (A.charAt(i - 1) == B.charAt(j - 1)) {
                    arr[j][i] = arr[j - 1][i - 1] + 1;
                } else {
                    arr[j][i] = Math.max(arr[j][i - 1], arr[j - 1][i]);
                }
            }
        }

        return arr[lengthB][lengthA];
    }

}
