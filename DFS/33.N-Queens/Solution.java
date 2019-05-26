public class Solution {
    /*
     * @param n: The number of queens
     * @return: All distinct solutions
     */
    private List<List<String>> result = new ArrayList<>();

    public List<List<String>> solveNQueens(int n) {
        // write your code here
        if (n <= 0) return result;
        helper(n, new ArrayList<Integer>());
        return result;
    }


    private void helper(int n, List<Integer> solution) {

        if (solution.size() == n) {
            // base case:
            result.add(drawBoard(solution, n));
            return;
        }

        // recursive case:
        for (int col = 0; col < n; col++) {
            if (!isSafe(col, solution)) {
                continue;
            }

            // choose
            solution.add(col);

            // explore
            helper(n, solution);

            // un-choose
            solution.remove(solution.size() - 1);
        }

    }


    private boolean isSafe(int col, List<Integer> solution) {
        int row = solution.size();
        for (int rowIndex = 0; rowIndex < solution.size(); rowIndex++) {
            if (solution.get(rowIndex) == col || rowIndex + solution.get(rowIndex) == row + col || rowIndex - solution.get(rowIndex) == row - col) {
                return false;
            }
        }
        return true;
    }


    private List<String> drawBoard(List<Integer> solution, int n) {
        List<String> result = new ArrayList<>();

        for (int i = 0; i < n; i++) {

            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < n; j++) {
                sb.append(j == solution.get(i) ? 'Q' : '.');
            }

            result.add(sb.toString());
        }

        return result;
    }


}





/**
* 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/

class Solution {
    /**
     * Get all distinct N-Queen solutions
     * @param n: The number of queens
     * @return: All distinct solutions
     * For example, A string '...Q' shows a queen on forth position
     */
    List<List<String>> solveNQueens(int n) {
        List<List<String>> results = new ArrayList<>();
        if (n <= 0) {
            return results;
        }

        search(results, new ArrayList<Integer>(), n);
        return results;
    }

    /*
     * results store all of the chessboards
     * cols store the column indices for each row
     */
    private void search(List<List<String>> results,
                        List<Integer> cols,
                        int n) {
        if (cols.size() == n) {
            results.add(drawChessboard(cols));
            return;
        }

        for (int colIndex = 0; colIndex < n; colIndex++) {
            if (!isValid(cols, colIndex)) {
                continue;
            }
            cols.add(colIndex);
            search(results, cols, n);
            cols.remove(cols.size() - 1);
        }
    }

    private List<String> drawChessboard(List<Integer> cols) {
        List<String> chessboard = new ArrayList<>();
        for (int i = 0; i < cols.size(); i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < cols.size(); j++) {
                sb.append(j == cols.get(i) ? 'Q' : '.');
            }
            chessboard.add(sb.toString());
        }
        return chessboard;
    }

    private boolean isValid(List<Integer> cols, int column) {
        int row = cols.size();
        for (int rowIndex = 0; rowIndex < cols.size(); rowIndex++) {
            if (cols.get(rowIndex) == column) {
                return false;
            }
            if (rowIndex + cols.get(rowIndex) == row + column) {
                return false;
            }
            if (rowIndex - cols.get(rowIndex) == row - column) {
                return false;
            }
        }
        return true;
    }
}
