public class SymmetricTree{
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
        public boolean isSymmetric(TreeNode root) {
            if (root == null) return true;

            Queue<TreeNode> stk = new LinkedList();
            stk.offer(root);
            stk.offer(root);


            while (!stk.isEmpty()){
                TreeNode l = stk.poll();
                TreeNode r = stk.poll();

                if (l == null && r == null)
                    continue;
                if (l == null || r == null)
                    return false;
                if (l.val != r.val)
                    return false;
                else{
                    stk.add(l.left);
                    stk.add(r.right);
                    stk.add(l.right);
                    stk.add(r.left);
                }

            }
            return true;

        }
    }
}