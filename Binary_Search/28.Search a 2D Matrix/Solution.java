public class Solution {
    /**
     * @param matrix: matrix, a list of lists of integers
     * @param target: An integer
     * @return: a boolean, indicate whether matrix contains target
     */
    public boolean searchMatrix(int[][] matrix, int target) {
        // write your code here
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return false;
        
        int row = matrix.length;
        int col = matrix[0].length;

        if (row == 1) {
            if (binarySearch(target, matrix[0]) != -1) {
                return true;
            } else {
                return false;
            }
        }

        if (target < matrix[0][0] || target > matrix[row - 1][col - 1]) return false;

        // Binary Search to find which row
        
        int[] colVector = new int[row];
        for (int i = 0; i < row; i++) {
            colVector[i] = matrix[i][0];
        }
        
        int rowNum = binarySearchInCol(target, colVector);


        if (binarySearch(target, matrix[rowNum]) != -1) {
            return true;
        } else {
            return false;
        }
        
        
    }

    private int binarySearchInCol(int target, int[] nums) {
        int start = 0, end = nums.length - 1;
        
        while (start + 1 < end) {
            int mid = (end - start) / 2 + start;
            
            if (target < nums[mid]) {
                end = mid;
            } else if (target > nums[mid]) {
                start = mid;
            } else {
                return mid;
            }
        }
        
        if (target < nums[end]) {
            return start;
        } else {
            return end;
        }
        
    }
    
    // Binary Search
    private int binarySearch(int target, int[] nums) {

        int start = 0, end = nums.length - 1;

        while (start + 1 < end) {
            int mid = (end - start) / 2 + start;

            if (target == nums[mid]) {
                return mid;
            } else if (target < nums[mid]) {
                end = mid;
            } else {
                start = mid;
            }
        }

            if (target == nums[start]) {
                return start;
            }

            if (target == nums[end]) {
                return end;
            }

            return -1;
    }

}





public class Solution {
    /**
     * @param matrix: matrix, a list of lists of integers
     * @param target: An integer
     * @return: a boolean, indicate whether matrix contains target
     */
    public boolean searchMatrix(int[][] matrix, int target) {
        // write your code here
        if (matrix == null || matrix.length == 0) return false;
        
        List<Integer> list = new ArrayList<Integer>();
        for (int i = 0; i < matrix.length; i++) {
            // tiny change 1: proper dimensions
            for (int j = 0; j < matrix[i].length; j++) { 
                // tiny change 2: actually store the values
                list.add(matrix[i][j]); 
            }
        }
    
        int[] vector = new int[list.size()];
        for (int i = 0; i < vector.length; i++) {
            vector[i] = list.get(i);
        }
        
        if (binarySearch(target, vector) != -1) {
            return true;
        } else {
            return false;
        }
    }

    // Binary Search
    private int binarySearch(int target, int[] nums) {

        int start = 0, end = nums.length - 1;

        while (start + 1 < end) {
            int mid = (end - start) / 2 + start;

            if (target == nums[mid]) {
                return mid;
            } else if (target < nums[mid]) {
                end = mid;
            } else {
                start = mid;
            }
        }

            if (target == nums[start]) {
                return start;
            }

            if (target == nums[end]) {
                return end;
            }

            return -1;
    }

}