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
            traverse(root.left, left);
        }

        if (root.right != null) {
            List<Integer> right = new ArrayList<>(path);
            right.add(root.val);
            traverse(root.right, right);
        }

    }

}




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

class ResultType {
    public int sum;
    public List<Integer> path;
    public ResultType(int sum, List<Integer> path) {
        this.sum = sum;
        this.path = path;
    }
}

public class Solution {
    /*
     * @param root: the root of binary tree
     * @param target: An integer
     * @return: all valid paths
     */
    private List<List<Integer>> results = new ArrayList<List<Integer>>();

    public List<List<Integer>> binaryTreePathSum(TreeNode root, int target) {
        // write your code here
        if (root == null) return results;
        
        List<Integer> path = new ArrayList<>();
        path.add(root.val);
        ResultType res = new ResultType(root.val, path);

        helper(root, target, res);
        System.out.println(results);
        return results;
        
    }

    private ResultType helper(TreeNode root, int target, ResultType res) {

        // leaf nodes
        if (root.left == null && root.right == null) {
            if (res.sum == target) {
                List<Integer> curr = new ArrayList<>(res.path);
                results.add(curr);
            }
            return res;
        }

        // Split
        if (root.left != null) {
            List<Integer> leftpath = new ArrayList<>(res.path);
            leftpath.add(root.left.val);
            ResultType left = new ResultType(res.sum + root.left.val, leftpath);
            helper(root.left, target, left);
        }

        if (root.right != null) {
            List<Integer> rightpath = new ArrayList<>(res.path);
            rightpath.add(root.right.val);
            ResultType right = new ResultType(res.sum + root.right.val, rightpath);
            helper(root.right, target, right);
        }

        return res;
    }

}



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

    public List<List<Integer>> binaryTreePathSum(TreeNode root, int target) {
        // write your code here
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;

        ArrayList<Integer> path = new ArrayList<Integer>();
        path.add(root.val);

        helper(root, path, root.val, target, result);
        return result;
    }

    private void helper(TreeNode root,
                        ArrayList<Integer> path,
                        int sum,
                        int target,
                        List<List<Integer>> result) {

        // leaf nodes
        if (root.left == null && root.right == null) {
            if (sum == target) {
                result.add(new ArrayList<Integer>(path));
            }
        }


        // go left
        if (root.left != null) {
            path.add(root.left.val);
            helper(root.left, path, sum + root.left.val, target, result);
            path.remove(path.size() - 1);
        }

        // go right
        if (root.right != null) {
            path.add(root.right.val);
            helper(root.right, path, sum + root.right.val, target, result);
            path.remove(path.size() - 1);
        }

    }

}
