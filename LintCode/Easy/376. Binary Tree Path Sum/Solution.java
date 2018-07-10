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
    /*
     * @param root: the root of binary tree
     * @param target: An integer
     * @return: all valid paths
     */
    
    List<List<Integer>> paths = new ArrayList<List<Integer>>();
    public List<List<Integer>> binaryTreePathSum(TreeNode root, int target) {
        // write your code here

        List<Integer> path = new ArrayList<Integer>();
        if (root == null) return paths;

        traverse(root, path);

        List<List<Integer>> results = new ArrayList<List<Integer>>();
        for (List<Integer> list : paths) {
            int sum  = list.stream().mapToInt(Integer::intValue).sum();
            if (sum == target) {
                results.add(list);
            }
        }

        return results;
    }

    // Definition: find all paths in subtrees
    private void traverse(TreeNode root, List<Integer> path) {
        // Exit when traverse to leaf nodes
        if (root.left == null && root.right == null) {
            List<Integer> currPath = new ArrayList<> (path);
            currPath.add(root.val);
            paths.add(currPath);
            return;
        }

        // Split
        if (root.left != null) {
            List<Integer> left = new ArrayList<>(path);
            left.add(root.val);
            traverse(root.left, left); // [1]  [1,2]
        }

        if (root.right != null) {
            List<Integer> right = new ArrayList<>(path);
            right.add(root.val);
            traverse(root.right, right);
        }

    }
    
    
    
}