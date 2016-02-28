

import java.util.HashMap;

public class StrobogrammaticNumber {
	public boolean isStrobogrammatic(String num) {
        HashMap<Character, Character> map = new HashMap<Character, Character>();
        map.put('0', '0');
        map.put('1', '1');
        map.put('8', '8');
        map.put('6', '9');
        map.put('9', '6');
        
        int n = num.length();
        int left = 0, right = n - 1;
        
        while (left <= right){
            if (map.containsKey(num.charAt(right)) && num.charAt(left) == map.get(num.charAt(right))){
                ++left;
                --right;
            }
            else{
                return false;
            }
        }
        return true;
    }
}
