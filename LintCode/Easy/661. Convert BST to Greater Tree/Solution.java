/**
* 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/

/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */

public class Solution {
    /**
     * @param root the root of binary tree
     * @return the new root
     */
    public int sum = 0;

    void helper(TreeNode root){
        if (root == null) {
            return;
        }
        if (root.right != null) {
            helper(root.right);
        }

        root.val = (sum += root.val);
        if (root.left != null) {
            helper(root.left);
        }
    }

    public TreeNode convertBST(TreeNode root) {
        // Write your code here
        helper(root);
        return root;
    }
}

// version: 高频题班
public class Solution {
    /**
     * @param root the root of binary tree
     * @return the new root
     */
    int sum = 0;

    void dfs(TreeNode cur) {
        if (cur == null) {
            return;
        }
        dfs(cur.right);
        sum += cur.val;
        cur.val = sum;
        dfs(cur.left);
    }

    public TreeNode convertBST(TreeNode root) {
        // Write your code here
        dfs(root);
        return root;
    }
}
