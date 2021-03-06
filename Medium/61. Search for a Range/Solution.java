public class Solution {
    /**
     * @param A: an integer sorted array
     * @param target: an integer to be inserted
     * @return: a list of length 2, [index1, index2]
     */
    public int[] searchRange(int[] A, int target) {
        // write your code here
        if (A == null || A.length == 0) {
            return new int[]{-1, -1};
        }

        int startIndex, endIndex, start = 0, end = A.length - 1;
        startIndex = binarySearch(A, target, start, end, true);
        endIndex = binarySearch(A, target, start, end, false);

        return new int[]{startIndex, endIndex};
    }


    private int binarySearch(int[] A, int target, int start, int end, boolean flag) {

        while (start + 1 < end) {
            int mid = (end - start) / 2 + start;

            if (target > A[mid]) {
                start = mid;
            } else if (target < A[mid]) {
                end = mid;
            } else {
                if (flag) {
                    end = mid;
                } else {
                    start = mid;
                }
            }

        }


        if (flag) {
            if (target == A[start]) {
                return start;
            }
            if (target == A[end]) {
                return end;
            }
            return -1;

        } else {
            if (target == A[end]) {
                return end;
            }
            if (target == A[start]) {
                return start;
            }
            return -1;
        }

    }


}
