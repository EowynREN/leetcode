import java.util.Arrays;

public class ThreeSumSmaller {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	public static int threeSumSmaller(int[] nums, int target) {
        int n = nums.length;
        if (n < 3){
            return 0;
        }
        
        Arrays.sort(nums);
        int count = 0;
        for (int i = 0; i < n - 2; ++i){
            int left = i + 1, right = n - 1;
            
            while (left < right){
                // if nums[i] + nums[left] + nums[right] < target
                // each item k between left and right
                // its sum nums[i] + nums[left] + nums[k] must < target
                if (nums[i] + nums[left] + nums[right] < target){
                    count += right - left;
                    ++left;
                }
                else{
                    --right;
                }
            }
        }
        return count;
    }

}
