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
     * @paramn n: An integer
     * @return: A list of root
     */
    public List<TreeNode> generateTrees(int n) {
        // write your code here
        return generate(1, n);
    }

    private List<TreeNode> generate(int start, int end){
        List<TreeNode> result = new ArrayList<TreeNode>();

        if (start > end) {
            result.add(null);
            return result;
        }

        if (start == end) {
            result.add(new TreeNode(start));
            return result;
        }

        List<TreeNode> left, right;
        for(int i = start; i <= end; i++){
            left  = generate(start, i - 1);
            right = generate(i + 1, end);
            for(TreeNode l: left){
                for(TreeNode r: right){
                    TreeNode root = new TreeNode(i);
                    root.left  = l;
                    root.right = r;
                    result.add(root);
                }
            }
        }
        return result;
    }

}
