import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Toposort {
    private ArrayList<Integer>[] adj;
    private ArrayList<Integer> topnum;
    private int[] visited;
    private int num;
    
    public Toposort(ArrayList<Integer>[] adj_) {
        adj = adj_;
        visited = new int[adj_.length];
        for (int i = 0; i < adj_.length; i++) {
            visited[i] = -1;
        }
        topnum = new ArrayList<>();
        for (int i = 0; i < adj_.length; i++) {
            topnum.add(-1);
        }
        num = adj_.length;
        
    }
    
    private ArrayList<Integer> toposort() {
        int length = adj.length;
        ArrayList<Integer> order = new ArrayList<Integer>();
        for (int i = 0; i < length; i++) {
            order.add(-1);
        }
        for (int i = 0; i < length; i++) {
            if (visited[i] == -1) {
                DFS(i);
            }
        }
        for (int i = 0; i < length; i++) {
            order.set(topnum.get(i)-1, i);
        }
        return order;
    }
    
    private void DFS(int i) {
        visited[i] = 0;
        for (int v: adj[i]) {
            if (visited[v] == -1) {
                DFS(v);
            }
        }
        topnum.set(i, num);
        num -= 1;
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
        Toposort top = new Toposort(adj);
        ArrayList<Integer> order = top.toposort();
        for (int x : order) {
            System.out.print((x + 1) + " ");
        }
    }
}
