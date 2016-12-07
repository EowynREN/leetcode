
public class LT544TopkLargestNumbers {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		MySolution s = new MySolution();
		int[] a = {3,10,1000,-99,4,100};
		int[] res = s.topk(a, 3);
		for(int i = 0; i <res.length ; ++i){
			System.out.println(res[i]);
		}
	}

}

class MySolution {
    /*
     * @param nums an integer array
     * @param k an integer
     * @return the top k largest numbers in array
     */
    public int[] topk(int[] nums, int k) {
        // Write your code here
        quickSort(nums, 0, nums.length - 1);
        int[] res = new int[k];
        
        for (int i = 0; i < k && i < nums.length; ++i){
            res[i] = nums[i];
        }
        return res;
    }
    
    public void quickSort(int[] nums, int left, int right){
        if (left >= right){
            return;
        }
        
        int i = left, j = right;
        int pivot = nums[(left + right) / 2];
        
        while (i <= j){
            while (i <= j && nums[i] > pivot){
                i++;
            }
            
            while (i <= j && nums[j] < pivot){
                j--;
            }
            
            if (i <= j){
                swap(nums, i, j);
                i++;
                j--;
            }
        }
        
        quickSort(nums, left, j);
        quickSort(nums, i, right);
    }
    
    public void swap(int[] nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
};


