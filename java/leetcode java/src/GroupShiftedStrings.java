import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

public class GroupShiftedStrings {
	public List<List<String>> groupStrings(String[] strings) {
        HashMap<String, List<String>> map = new HashMap<String, List<String>>();
        List<List<String>> res = new ArrayList<List<String>>();
        
        for (String str : strings){
            String code = encode(str);
            if (map.containsKey(code)){
                map.get(code).add(str);
            }
            else{
                List<String> temp = new ArrayList<String>();
                temp.add(str);
                map.put(code, temp);
            }
        }
        
        for (String key: map.keySet()){
            List<String> temp = map.get(key);
            Collections.sort(temp);
            res.add(temp);
        }
        return res;
    }
    
    public String encode(String str){
        int n = str.length();
        if (n == 1) return "a";
        
        String res  = "a";
        for (int i = 0; i < n - 1; ++i){
            int t = str.charAt(i + 1) - str.charAt(i);
            //in case ["az", "ba"]
            if (t < 0){
                t += 26;
            }
            res += (char)(t + 97);
        }
        return res;
    }

}
