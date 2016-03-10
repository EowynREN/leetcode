import java.util.ArrayList;
import java.util.List;

public class SummaryRanges {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	public static List<String> summaryRanges(int[] nums) {
        List<String> res = new ArrayList<String>();
        for (int i = 0; i < nums.length; ++i){
            int p = nums[i];
            
            while (i < nums.length - 1 && nums[i + 1] - nums[i] == 1){
                ++i;
            }
            
            if (p == nums[i]){
                res.add(nums[i] + "");
            }
            else{
                res.add(p + "->" + nums[i]);
            }
        }
        return res;
    }

}
