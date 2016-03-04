import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Flatten2DVector {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		List<List<Integer>> vec2d = new ArrayList<List<Integer>>();
		List<Integer> v = new ArrayList<>();
		v.add(1);
		v.add(4);
		v.add(3);
		v.add(5);
		List<Integer> v1 = new ArrayList<>();
		v1.add(7);
		v1.add(10);
		v1.add(2);
		
		vec2d.add(v);
		vec2d.add(v1);
		
		Vector2D i = new Vector2D(vec2d);
		while (i.hasNext()){
			int t = i.next();
		}
	}
}

class Vector2D {
    private Iterator<List<Integer>> i;
    private Iterator<Integer> j;
    
    public Vector2D(List<List<Integer>> vec2d) {
        this.i = vec2d.iterator();
    }

    public int next() {
        hasNext();
        return j.next();
    }

    public boolean hasNext() {
        //j == null 表示刚开始遍历，指针指到第一行, 或当前list为空，eg, [[], [3]]
        //!j.hasNext()表示i行已遍历完，指针指到i + 1行
        //i.hasNext()表示还有行没有遍历，若已遍历完，则判断j.hasNext()（return处）
                                                    // 若j.hasNext()也没有，则整个Vector2D遍历完成
        while ((j == null || !j.hasNext()) && i.hasNext()){
            j = i.next().iterator();
        }
        //j == null表示i的迭代器中没有元素，为[]
        return j != null && j.hasNext();
    }
}