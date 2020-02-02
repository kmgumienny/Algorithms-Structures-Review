public class SameTree{
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
        public boolean isSameTree(TreeNode p, TreeNode q) {
            if(p == null && q == null)
                return true;
            else if(p == null || q == null)
                return false;

            Stack<TreeNode> tp = new Stack();
            Stack<TreeNode> tq = new Stack();
            tp.push(p);
            tq.push(q);

            while (!tp.isEmpty() && !tq.isEmpty()){
                TreeNode nodep = tp.pop();
                TreeNode nodeq = tq.pop();

                if (nodep.val != nodeq.val || tq.size() != tp.size())
                    return false;

                if (nodep.left != null && nodeq.left !=null){
                    tq.push(nodeq.left);
                    tp.push(nodep.left);
                } else if (nodep.left != null || nodeq.left !=null) return false;

                if (nodep.right != null && nodeq.right !=null){
                    tq.push(nodeq.right);
                    tp.push(nodep.right);
                } else if (nodep.right != null || nodeq.right !=null) return false;
            }
            return true;

        }
    }
}