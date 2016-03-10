import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Stack;

public class AlienDictionary {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		String[] words = {"abandon", "abyss", "smart", "star", "xxy", "xy"};
//		String[] words = {"wrt", "wrf", "er", "ett", "rftt"};
		String[] words = {""};
		
		Solution s = new Solution();
		System.out.println(s.alienOrder(words));
	}

}

class Solution {
	HashMap<Character, GraphNode> map = new HashMap<>();
    HashMap<Character, Integer> indegree = new HashMap<>();
    public String alienOrder(String[] words) {       
        for (int i = 0; i < words.length - 1; ++i){
            for (int j = 0; j < Math.min(words[i].length(), words[i + 1].length()); ++j){
                char first = words[i].charAt(j);
                char second = words[i + 1].charAt(j);
                
                if (!map.containsKey(first)){
                    GraphNode f = new GraphNode(first);
                    f.adj = new ArrayList<GraphNode>();
                    map.put(first, f);
                }
                if (!map.containsKey(second)){
                    GraphNode s = new GraphNode(second);
                    s.adj = new ArrayList<GraphNode>();
                    map.put(second, s);
                }
                
                if (first != second){
                    GraphNode prev = map.get(first);
                    GraphNode next = map.get(second);
                    prev.adj.add(next);
                    
                    if (indegree.containsKey(first)){
                        int count = indegree.get(first) + 1;
                        indegree.put(first, count);
                    }
                    else{
                        indegree.put(first, 0);
                    }
                    
                    if (indegree.containsKey(second)){
                        int count = indegree.get(second) + 1;
                        indegree.put(second, count);
                    }
                    else{
                        indegree.put(second, 1);
                    }
                    break;
                }
            }
        }
//        for (Character key: map.keySet()){
//            if (!indegree.containsKey(key)){
//                indegree.put(key, 0);
//            }
//        }
        return topologicalSort();
    }
    
    public String topologicalSort(){
        String res = "";
        Queue<GraphNode> q = new ArrayDeque<>();
        for (Map.Entry<Character, Integer> entry : indegree.entrySet()){
            if (entry.getValue() == 0){
                ((ArrayDeque) q).push(map.get(entry.getKey()));
            }
        }
        
        while (!q.isEmpty()){
            GraphNode node = ((ArrayDeque<GraphNode>) q).pop();
            res += node.val;
            
            Iterator<GraphNode> it = node.adj.iterator();
            while (it.hasNext()){
                GraphNode in = it.next();
                int count = indegree.get(in.val) - 1;
                indegree.put(in.val, count);
                if (count == 0){
                    ((ArrayDeque<GraphNode>) q).push(map.get(in.val));
                }
            }
        }
        return res;
    }
    
    public boolean dfs(){
    	Stack<GraphNode> stack = new Stack<>();
    	if ((GraphNode) map.entrySet().toArray()[0] != null){
    		stack.push((GraphNode) map.entrySet().toArray()[0]);
    	}
    	
    	while (!stack.isEmpty()){
    		
    	}
    }
}

class GraphNode{
    char val;
    List<GraphNode> adj;
    GraphNode(char x) { val = x; }
}
