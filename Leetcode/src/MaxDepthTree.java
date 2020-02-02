public class MaxDepthTree {
    /**
     * Definition for a binary tree node.
     * public class TreeNode {
     *     int val;
     *     TreeNode left;
     *     TreeNode right;
     *     TreeNode(int x) { val = x; }
     * }
     */
    class Solution {
        public int maxDepth(TreeNode root) {
            if (root == null)
                return 0;
            return recurseTree(root, 0);
        }

        public static int recurseTree(TreeNode root, int val){
            if (root == null)
                return 0;
            return Integer.max(recurseTree(root.left, 0), recurseTree(root.right, 0)) + 1;
        }
    }
}