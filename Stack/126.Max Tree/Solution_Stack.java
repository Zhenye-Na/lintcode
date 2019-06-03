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
     * @param A: Given an integer array with no duplicates.
     * @return: The root of max tree.
     */
    public TreeNode maxTree(int[] A) {
        // write your code here
        if (A == null || A.length == 0) {
            return null;
        }

        Stack<TreeNode> stack = new Stack<>();
        for (int i = 0; i < A.length; i++) {
            // 遍历 A 的每个元素, 创造结点 node
            TreeNode node = new TreeNode(A[i]);

            // 将 stack 中小于当前结点的结点都 pop 出来, 存为当前结点的左子树
            while (!stack.isEmpty() && node.val >= stack.peek().val) {
                node.left = stack.pop();
            }

            // 如果 stack 仍非空, 剩下的结点一定大于 node, 所以将 node 存为 stack 中结点的右子树;
            // 如果栈中有大于等于2个元素, 栈顶节点自身的右子树, 现在变成了 node 的左子树
            // 栈不空, 栈中还有比遍历到的节点值更大的节点, 那么就要把 node 变成 栈顶节点的右子树
            if (!stack.isEmpty()) {
                stack.peek().right = node;
            }

            // stack 中存放结点的顺序为: 底部为完整的 max tree, 从下向上是下一层孩子结点的备份, 顶部是当前结点的备份
            stack.push(node);
        }

        TreeNode root = stack.pop();
        while (!stack.isEmpty()) {
            root = stack.pop();
        }
        return root;
    }
}