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


// Solution 1: Traverse helper function - Template 1

public class Solution {
    /**
     * @param root: A Tree
     * @return: Preorder in ArrayList which contains node values.
     */
    public List<Integer> preorderTraversal(TreeNode root) {
        // write your code here
        List<Integer> result = new ArrayList<>();
        traverse(root, result);
        return result;

    }

    private void traverse(TreeNode root, List<Integer> result) {
        // return if current root is null.
        if (root == null) {
            return;
        }

        // 根 -> 左 -> 右
        result.add(root.val);
        traverse(root.left, result);
        traverse(root.right, result);
    }

}


// Solution 2: Dicide and Conquer - Template 2

public class Solution {
    /**
     * @param root: A Tree
     * @return: Preorder in ArrayList which contains node values.
     */
    public List<Integer> preorderTraversal(TreeNode root) {
        // write your code here
        // Divide and Conquer
        List<Integer> result = new ArrayList<Integer> ();
        if (root == null) {
            return result;
        }

        List<Integer> left = preorderTraversal(root.left);
        List<Integer> right = preorderTraversal(root.right);

        result.add(root.val);
        result.addAll(left);
        result.addAll(right);

        return result;
        
    }

}


// Solution 3: Non-Recursive (Stack)

public class Solution {
    /**
     * @param root: A Tree
     * @return: Preorder in ArrayList which contains node values.
     */
    public List<Integer> preorderTraversal(TreeNode root) {
        // write your code here
        // Divide and Conquer
        List<Integer> result = new ArrayList<Integer> ();
        Stack<TreeNode> NodeStack = new Stack<TreeNode> ();
        
        if (root == null) {
            return result;
        }

        NodeStack.push(root);
        
        while (!NodeStack.isEmpty()) {

            TreeNode node = NodeStack.pop();
            result.add(node.val);

            if (node.right != null) NodeStack.push(root.right);
            if (node.left != null) NodeStack.push(root.left);

        }

        return result;
        
    }

}