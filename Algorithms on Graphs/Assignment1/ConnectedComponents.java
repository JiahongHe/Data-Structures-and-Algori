import java.util.ArrayList;
import java.util.Scanner;

public class ConnectedComponents {
    private ArrayList<Integer>[] adj;
    private ArrayList<ArrayList<Integer>> connected;
    private ArrayList<Integer> visited;
    private ArrayList<Integer> reachable;
    
    public ConnectedComponents(ArrayList<Integer>[] adj_) {
        adj = adj_;
        connected = new ArrayList<>();
        visited = new ArrayList<>();
        reachable = new ArrayList<>();
    }
    
    public void DFS(int i) {
        visited.add(i);
        reachable.add(i);
        for (int v: adj[i]) {
            if (!visited.contains(v)) {
                DFS(v);
            }
        }
    }
    
    public ArrayList<Integer> findConnected(int i) {
        reachable.clear();
        DFS(i);
        return reachable;
    }
    
    public void findAllConnected() {
        connected.clear();
        visited.clear();
        for (int i = 0; i < adj.length; i++) {
            if (!visited.contains(i)) {
                connected.add(findConnected(i));
            }
        }
    }
    
    private int numberOfComponents() {
        findAllConnected();
        return connected.size();
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
        ConnectedComponents g = new ConnectedComponents (adj);
        System.out.println((g.numberOfComponents()));
    }
}

