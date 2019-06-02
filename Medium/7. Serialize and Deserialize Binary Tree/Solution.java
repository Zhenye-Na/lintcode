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
     * This method will be invoked first, you should design your own algorithm 
     * to serialize a binary tree which denote by a root node to a string which
     * can be easily deserialized by your own "deserialize" method later.
     */
    public String serialize(TreeNode root) {
        // write your code here
        if (root == null) return "{}";

        List<TreeNode> queue = new ArrayList<>();
        queue.add(root);

        for (int i = 0; i < queue.size(); i++) {
            TreeNode node = queue.get(i);
            if (node != null) {
                queue.add(node.left);
                queue.add(node.right);
            }
        }

        while (queue.get(queue.size() - 1) == null) {
            queue.remove(queue.size() - 1);
        }

        StringBuilder sb = new StringBuilder();

        sb.append("{");
        sb.append(queue.get(0).val);

        for (int i = 1; i < queue.size(); i++) {
            if (queue.get(i) == null) {
                sb.append(",#");
            } else {
                sb.append(",");
                sb.append(queue.get(i).val);
            }
        }

        sb.append("}");
        return sb.toString();
    }

    /**
     * This method will be invoked second, the argument data is what exactly
     * you serialized at method "serialize", that means the data is not given by
     * system, it's given by your own serialize method. So the format of data is
     * designed by yourself, and deserialize it here as you serialize it in 
     * "serialize" method.
     */
    public TreeNode deserialize(String data) {
        // write your code here
        if (data.equals("{}")) {
            return null;
        }
        
        // remove "{" and "}"
        String[] nodeArray = data.substring(1, data.length() - 1).split(",");
        List<TreeNode> nodeList = new ArrayList<>();

        TreeNode root = new TreeNode(Integer.parseInt(nodeArray[0]));
        nodeList.add(root);

        int flag = 0;  // left or right
        int parentID = 0;

        for (int index = 1; index < nodeArray.length; index++) {
            String s = nodeArray[index];

            if (!s.equals("#")) {
                TreeNode node = new TreeNode(Integer.parseInt(s));
                
                if (flag % 2 == 0) {  // left child
                    nodeList.get(parentID).left = node;
                    flag++;
                } else {              // right child
                    nodeList.get(parentID).right = node;
                    flag++;
                }
                nodeList.add(node);                
            } else {
                flag++;
            }
            
            if (flag % 2 == 0) parentID++;
            
        }
        
        return root;

    }
}