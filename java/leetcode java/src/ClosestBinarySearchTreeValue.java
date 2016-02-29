
public class ClosestBinarySearchTreeValue {
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	public static int closestValue(TreeNode root, double target) {
        int closest = root.val;
        
        while (root != null){
            //当前最近值小于之前的最近值
            if (Math.abs(target - root.val) < Math.abs(target - closest)){
                closest = root.val;
            }
            root = target > root.val ? root.right : root.left;
        }
        return closest;
    }

	 class TreeNode {
		 int val;
	     TreeNode left;
	     TreeNode right;
	     TreeNode(int x) { val = x; }
	 }
}
