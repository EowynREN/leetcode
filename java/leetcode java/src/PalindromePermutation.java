import java.util.HashSet;

public class PalindromePermutation {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	public static boolean canPermutePalindrome(String s) {
        HashSet set = new HashSet();
        
        for (int i = 0; i < s.length(); ++i){
            if (set.contains(s.charAt(i))){
                set.remove(s.charAt(i));
            }
            else{
                set.add(s.charAt(i));
            }
        }
        return set.size() <= 1;
    }

}
