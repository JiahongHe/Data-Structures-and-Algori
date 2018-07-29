import java.util.ArrayList;
import java.util.Scanner;

public class Acyclicity {
    private ArrayList<Integer>[] adj;
    private ArrayList<Integer> visited;
    
    public Acyclicity(ArrayList<Integer>[] adj_) {
        adj = adj_;
        visited = new ArrayList<>();
        for (int i = 0; i < adj.length; i++) {
            visited.add(-1);
        }
    }
    
    private boolean DFS(int i) {
        for (int v: adj[i]) {
            if (visited.get(v) == -1) {
                visited.set(v, 0);
                boolean found = DFS(v);
                visited.set(v, 1);
                if (found) {
                    return true;
                }
            }
            if (visited.get(v) == 0) {
                return true;
            }
        }
        return false;
    }
    
    private int acyclic() {
        for (int i = 0; i < adj.length; i++) {
            visited.set(i, 0);
            boolean found = DFS(i);
            if (found) {
                return 1;
            }
            visited.set(i, 1);
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
        }
        Acyclicity acy = new Acyclicity(adj);
        System.out.println(acy.acyclic());
    }
}
