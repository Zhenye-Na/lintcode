# 33. N-Queens


- **Description**
    - The `n-queens` puzzle is the problem of placing `n` queens on an `n×n` chessboard such that no two queens attack each other.
    - Given an integer `n`, return all **distinct** solutions to the `n-queens` puzzle.
    - Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space respectively.  
- **Example**
    - There exist two distinct solutions to the 4-queens puzzle:

    ```java
    [
      // Solution 1
      [".Q..",
       "...Q",
       "Q...",
       "..Q."
      ],
      // Solution 2
      ["..Q.",
       "Q...",
       "...Q",
       ".Q.."
      ]
    ]
    ```

- **Challenge**
    - Can you do it without recursion?


## Solution

**N-皇后问题**

这道题第一眼看上去不知从何下手，仔细思考一下可以用 `DFS+Recursion` 来做，提供个人思考思路以及代码实现（可惜空间复杂度太大，没有一击AC T_T）：

![](https://leetcode.com/static/images/problemset/8-queens.png)

- 如上图所示，是一个 `8阶-皇后` 问题，皇后在国际象棋据说非常 `diǎo`，`同一行，同一列，同一正/反对角线`，都不可以，所以以此作为条件。
- 从 `(0,0)` 开始搜索，然后下一个 `Queen` 的位置一定是在 `下一行` ，就可以套模板了。
- 虽然没有一击AC，但是还是提供“错误”代码以及详细 comments


### [Failed] Solution 1

```java
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

        // Exit when there is a Queen in each row of the chess board
        if (layout.size() == n) {
            results.add(new ArrayList<>(layout));
            return;
        }

        // Split
        for (int i = startX; i < n; i++) {
            for (int j = startY; j < n; j++) {
                // Current position coordinate
                Coordinate curr = new Coordinate(i, j);
                // The first row => layout.size() == 0, and whether this coordinate is valid according to all of the previous Queens
                if (layout.size() == 0 || isValid(layout, curr)) {
                    // Add this position to layout if valid
                    layout.add(curr);
                    // Attention, next Queen can only be in the next row
                    helper(n, i + 1, 0, layout, results);
                    // Remember to remove it after recursion
                    layout.remove(layout.size() - 1);
                }

            }
        }
    }


    private boolean isValid(List<Coordinate> layout, Coordinate curr) {
        for (Coordinate queen : layout) {
            // not in the same row && not in the same column || not in the diagnals
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
```


### Backtracking

```java
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
```

***


**贴上九章的题解，观摩大佬的答案：**

- 首先不需要存储**行数**，因为每行都有且仅有一个，而且DFS是从第0行到第n-1行


```java
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
```
