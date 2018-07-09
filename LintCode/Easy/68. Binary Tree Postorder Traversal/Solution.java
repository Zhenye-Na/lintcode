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
     * @param root: A Tree
     * @return: Postorder in ArrayList which contains node values.
     */
    public List<Integer> postorderTraversal(TreeNode root) {
        // write your code here
        
        List<Integer> result = new ArrayList<>();
        traverse(root, result);
        return result;
    }
    
    private void traverse(TreeNode root, List<Integer> result) {
        
        if (root == null) return;
        
        traverse(root.left, result);
        traverse(root.right, result);
        result.add(root.val);
        
    }
    
}


public class Solution {
    /**
     * @param root: A Tree
     * @return: Postorder in ArrayList which contains node values.
     */
    public List<Integer> postorderTraversal(TreeNode root) {
        // write your code here
        // Divide and Conquer
        
        List<Integer> result = new ArrayList<Integer>();
        
        if (root == null) return result;
        
        List<Integer> left = postorderTraversal(root.left);
        List<Integer> right = postorderTraversal(root.right);
        
        result.addAll(left);
        result.addAll(right);
        result.add(root.val);

        return result; 
    }

}