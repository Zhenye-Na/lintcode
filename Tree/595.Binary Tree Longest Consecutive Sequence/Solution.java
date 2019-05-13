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
     * @param root: the root of binary tree
     * @return: the length of the longest consecutive sequence path
     */

    private int length = 0;
    public int longestConsecutive(TreeNode root) {
        // write your code here
        helper(root);
        return length;
    }

    // Definition: find longest consecutive sequence in subtree
    private int helper(TreeNode root) {
        // Exit
        if (root == null) {
            return 0;
        }

        // Split
        int left = helper(root.left);
        int right = helper(root.right);

        int sublength = 1; // 记录当前根节点

        // 左子树非空，并且 根节点 与 左叶子节点值 相差 1
        if (root.left != null && root.val - root.left.val == -1) {
            sublength = Math.max(sublength, left + 1);
        }
        // 右子树非空，并且 根节点 与 右叶子节点值 相差 1
        if (root.right != null && root.val - root.right.val == -1) {
            sublength = Math.max(sublength, right + 1);
        }
        // 更新 全局变量
        if (sublength > length) {
            length = sublength;
        }
        // 返回 subtree 的长度
        return sublength;
    }

}






/**
* 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/

// version 1: Traverse + Divide Conquer
public class Solution {
    /**
     * @param root the root of binary tree
     * @return the length of the longest consecutive sequence path
     */
    public int longestConsecutive(TreeNode root) {
        return helper(root, null, 0);
    }

    private int helper(TreeNode root, TreeNode parent, int lengthWithoutRoot) {
        if (root == null) {
            return 0;
        }

        int length = (parent != null && parent.val + 1 == root.val)
            ? lengthWithoutRoot + 1
            : 1;
        int left = helper(root.left, root, length);
        int right = helper(root.right, root, length);
        return Math.max(length, Math.max(left, right));
    }
}





// version 2: Another Traverse + Divide Conquer
public class Solution {
    private int longest;

    /**
     * @param root the root of binary tree
     * @return the length of the longest consecutive sequence path
     */
    public int longestConsecutive(TreeNode root) {
        longest = 0;
        helper(root);
        return longest;
    }

    private int helper(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int left = helper(root.left);
        int right = helper(root.right);

        int subtreeLongest = 1; // at least we have root
        if (root.left != null && root.val + 1 == root.left.val) {
            subtreeLongest = Math.max(subtreeLongest, left + 1);
        }
        if (root.right != null && root.val + 1 == root.right.val) {
            subtreeLongest = Math.max(subtreeLongest, right + 1);
        }

        if (subtreeLongest > longest) {
            longest = subtreeLongest;
        }
        return subtreeLongest;
    }
}




// version 3: Divide Conquer
public class Solution {
    private class ResultType {
        int maxInSubtree;
        int maxFromRoot;
        public ResultType(int maxInSubtree, int maxFromRoot) {
            this.maxInSubtree = maxInSubtree;
            this.maxFromRoot = maxFromRoot;
        }
    }
    /**
     * @param root the root of binary tree
     * @return the length of the longest consecutive sequence path
     */
    public int longestConsecutive(TreeNode root) {
        return helper(root).maxInSubtree;
    }

    private ResultType helper(TreeNode root) {
        if (root == null) {
            return new ResultType(0, 0);
        }

        ResultType left = helper(root.left);
        ResultType right = helper(root.right);

        // 1 is the root itself.
        ResultType result = new ResultType(0, 1);

        if (root.left != null && root.val + 1 == root.left.val) {
            result.maxFromRoot = Math.max(
                result.maxFromRoot,
                left.maxFromRoot + 1
            );
        }

        if (root.right != null && root.val + 1 == root.right.val) {
            result.maxFromRoot = Math.max(
                result.maxFromRoot,
                right.maxFromRoot + 1
            );
        }

        result.maxInSubtree = Math.max(
            result.maxFromRoot,
            Math.max(left.maxInSubtree, right.maxInSubtree)
        );

        return result;
    }
}
