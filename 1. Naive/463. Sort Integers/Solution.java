public class Solution {
    /**
     * @param A: an integer array
     * @return: nothing
     */
    public void sortIntegers(int[] A) {
        // write your code here

        for (int i = 0; i < A.length; i++) {
            int min = A[i];
            int pos = i;
            for (int j = i; j < A.length; j++) {
                if (min > A[j]) {
                    min = A[j];
                    pos = j;
                }
            }
            
            int tmp = A[i];
            A[i] = A[pos];
            A[pos] = tmp;
            
        }

    }
}