import java.util.ArrayList;
import java.util.List;

public class FlipGameII {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	public static boolean canWin(String s) {
        List<Character> list = new ArrayList<>();
        for (int i = 0; i < s.length(); ++i){
            list.add(s.charAt(i));
        }
        return helper(list);
    }
    
    public static boolean helper(List<Character> list){
        for (int i = 0; i < list.size() - 1; ++i){
            if (list.get(i) == '+' && list.get(i + 1) == '+'){
                list.set(i, '-');
                list.set(i + 1, '-');
                
                //determine my winnese according to opponent's status
                //if opponent win, I lose
                //if opponent lose, I win
                boolean win = (!helper(list));
                
                list.set(i, '+');
                list.set(i + 1, '+');
                
                if (win) return true;
            }
        }
        //there is no valid move -> lose
        return false;
    }
}
