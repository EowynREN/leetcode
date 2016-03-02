
public class PaintFence {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	public static int numWays(int n, int k) {
        // base case
        // n = 1, k
        // n = 2, 2.1 k * 1                ----same
        //       2.2 k * (k - 1)          ----diff
        
        // build up      
        // n = 3, from 2.1, same * (k - 1) ----diff
        //       from 2.2, diff * 1       ----same => same = diff * 1,   diff = same * (k - 1) + diff * (k - 1)
        
        
        //0个篱笆
        if (n == 0){
            return 0;
        }
        
        //1个篱笆
        if (n == 1){
            return k;
        }
        
        //same + diff 2个篱笆
        int same = k, diff = k * (k - 1);
        
        //3 ~ n个篱笆
        for (int i = 3; i <= n; ++i){
            int temp = same;
            same = diff;
            diff = (temp + diff) * (k - 1);
        }
        return same + diff;
    }

}
