class Coordinate {
    public int x;
    public int y;
    public Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }
}


public class Solution {
    /*
     * @param n: The number of queens
     * @return: All distinct solutions
     */
    public List<List<String>> solveNQueens(int n) {
        // write your code here
        List<List<Coordinate>> results = new ArrayList<>();
        if (n <= 0) return new ArrayList<List<String>>();

        helper(n, 0, 0, new ArrayList<Coordinate>(), results);
        List<List<String>> layout = drawGrid(n, results);
        return layout;
    }

    
    private void helper(int n,
                        int startX,
                        int startY,
                        List<Coordinate> layout,
                        List<List<Coordinate>> results) {
        
        // Definition: Recursively find all possible ways to arrange Queens' position
        
        // Exit
        if (layout.size() == n) {
            results.add(new ArrayList<>(layout));
            return;
        }

        // Split
        for (int i = startX; i < n; i++) {
            for (int j = startY; j < n; j++) {
                Coordinate curr = new Coordinate(i, j);
                if (layout.size() == 0 || isValid(layout, curr)) {
                    layout.add(curr);
                    helper(n, i + 1, 0, layout, results);
                    layout.remove(layout.size() - 1);
                }
                
            }
        }
    }
    

    private boolean isValid(List<Coordinate> layout, Coordinate curr) {
        for (Coordinate queen : layout) {
            if (queen.x == curr.x || queen.y == curr.y || (curr.x + curr.y == queen.x + queen.y) || (curr.y - curr.x == queen.y - queen.x)) {
                return false;
            }
        }
        return true;
    }
    
    
    private List<List<String>> drawGrid(int n,
                                        List<List<Coordinate>> results) {
        
        // Draw chess board
        List<List<String>> layout = new ArrayList<>();
        
        for (int index = 0; index < results.size(); index++) {
            List<String> chessboard = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                StringBuilder sb = new StringBuilder();
                for (int j = 0; j < n; j++) {
                    sb.append(j == results.get(index).get(i).y ? 'Q' : '.');
                }
                chessboard.add(sb.toString());
            }
            layout.add(chessboard);
        }
        return layout;
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