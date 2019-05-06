public class Solution {
    /*
     * @param A: sorted integer array A
     * @param B: sorted integer array B
     * @return: A new sorted integer array
     */
    public int[] mergeSortedArray(int[] A, int[] B) {
        if (A == null || A.length == 0) {
            return B;
        }
        if (B == null || B.length == 0) {
            return A;
        }
 
        int[] res = new int[A.length + B.length];
        int idx = 0;
        int pa = 0;
 
        for(int i = 0; i < B.length; i++){
            int position = binarySearch(A, B[i]);
            while(pa < position){
                res[idx++] = A[pa++];
            }
            res[idx++] = B[i];
        }
 
        while(pa < A.length){
            res[idx++] = A[pa++];
        }
 
        return res;
    }
    
    private int binarySearch(int[] A, int target){
        int left = 0;
        int right = A.length-1;

        while(left <= right){
            int mid = left + (right-left)/2;
            if (A[mid] == target) {
                return mid;
            } else if (target < A[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}