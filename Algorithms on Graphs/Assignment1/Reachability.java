import java.util.ArrayList;
import java.util.Scanner;

public class Reachability {
    private ArrayList<Integer>[] adj;
    private ArrayList<Integer> reachable;
    
    public Reachability(ArrayList<Integer>[] adj_) {
        adj = adj_;
        reachable = new ArrayList<>();
    }
    
    private boolean find(ArrayList<Integer> arr, int v) {
        for (int i = 0; i < arr.size(); i++) {
            if (v == arr.get(i)) {
                return true;
            }
        }
        return false;
    }
    
    private void DFS(int i) {
        reachable.add(i);
        for (int v: adj[i]) {
            if (find(reachable, v)) {
                continue;
            }
            DFS(v);
        }
    }
    private int reach(int x, int y) {
        reachable.clear();
        DFS(x);
        if (find(reachable, y)) {
            return 1;
        }
        return 0;
    }
    
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        ArrayList<Integer>[] adj = (ArrayList<Integer>[])new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < m; i++) {
            int x, y;
            x = scanner.nextInt();
            y = scanner.nextInt();
            adj[x - 1].add(y - 1);
            adj[y - 1].add(x - 1);
        }
        int x = scanner.nextInt() - 1;
        int y = scanner.nextInt() - 1;
        Reachability reach_ = new Reachability(adj);
        System.out.println(reach_.reach(x, y));
    }
}
