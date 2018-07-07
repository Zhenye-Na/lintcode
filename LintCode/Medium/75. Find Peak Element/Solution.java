public class Solution {
    /*
     * @param A: An integers array.
     * @return: return any of peek positions.
     */
    public int findPeak(int[] A) {
        // write your code here
        if (A.length == 0) return -1;
        if (A.length == 3) return 1;
        
        
        int start = 0, end = A.length - 1;
        
        while (start + 1 < end) {
            
            int mid = (end - start) / 2 + start;
            
            if (A[mid - 1] < A[mid] && A[mid] < A[mid + 1]) {         // Ascending section
                start = mid;
            } else if (A[mid - 1] > A[mid] && A[mid] > A[mid + 1]) {  // Descending section
                end = mid;
            } else if (A[mid - 1] > A[mid] && A[mid] < A[mid + 1]) {  // Valley
                end = mid;
            } else {                                                  // Peak
                return mid;
            }
            
            
        }
        
        if (A[start] < A[end]) {
            return end;
        } else {
            return start;
        }

        
    }
}