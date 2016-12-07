import java.util.Comparator;
import java.util.PriorityQueue;

public class LT544TopkLargestNumbers2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TopK s = new TopK();
		int[] nums = {3,10,1000,-99,4,100};
		s.topk(nums, 3);
		
	}

}

class TopK {
    /*
     * @param nums an integer array
     * @param k an integer
     * @return the top k largest numbers in array
     */
    public int[] topk(int[] nums, int k) {
        // Write your code here
    	PriorityQueue<Integer> minHeap = new PriorityQueue(k, new MyComparator());
    	int[] res = new int[k];
    	
    	for (int i = 0; i < k; ++i){
    		minHeap.offer(nums[i]);
    	}
    	
    	for (int i = k; i < nums.length; ++i){
    		if (nums[i] > minHeap.peek()){
    			minHeap.poll();
    			minHeap.offer(nums[i]);
    		}
    	}
    	
    	for (int i = k - 1; i >= 0; --i){
    		res[i] = minHeap.poll();
    	}
    	return res;
    }
    
};

class MyComparator implements Comparator<Integer>{

	@Override
	public int compare(Integer o1, Integer o2) {
		// TODO Auto-generated method stub
		return o1 - o2;
	}
	
	
}


