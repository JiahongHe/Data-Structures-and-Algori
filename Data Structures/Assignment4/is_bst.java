import java.util.*;
import java.io.*;

public class is_bst {
    class FastScanner {
        StringTokenizer tok = new StringTokenizer("");
        BufferedReader in;
        
        FastScanner() {
            in = new BufferedReader(new InputStreamReader(System.in));
        }
        
        String next() throws IOException {
            while (!tok.hasMoreElements())
                tok = new StringTokenizer(in.readLine());
            return tok.nextToken();
        }
        int nextInt() throws IOException {
            return Integer.parseInt(next());
        }
    }
    
    public class IsBST {
        class Node {
            int key;
            int left;
            int right;
            
            Node(int key, int left, int right) {
                this.left = left;
                this.right = right;
                this.key = key;
            }
        }
        private ArrayList<Integer> res = new ArrayList<>();
        int nodes;
        Node[] tree;
        
        void read() throws IOException {
            FastScanner in = new FastScanner();
            nodes = in.nextInt();
            tree = new Node[nodes];
            for (int i = 0; i < nodes; i++) {
                tree[i] = new Node(in.nextInt(), in.nextInt(), in.nextInt());
            }
        }
        
        void inOrderTraverse(int i) {
            if (tree[i].left != -1) {
                inOrderTraverse(tree[i].left);
            }
            res.add(tree[i].key);
            if (tree[i].right != -1) {
                inOrderTraverse(tree[i].right);;
            }
        }
        boolean solve() {
            res.clear();
            if (tree.length <= 1) {
                return true;
            }
            inOrderTraverse(0);
            for (int i = 0; i < res.size() - 1; i++) {
                if (res.get(i) > res.get(i + 1)) {
                    return false;
                }
            }
            return true;
        }
    }
    
    static public void main(String[] args) throws IOException {
        new Thread(null, new Runnable() {
            public void run() {
                try {
                    new is_bst().run();
                } catch (IOException e) {
                }
            }
        }, "1", 1 << 26).start();
    }
    public void run() throws IOException {
        IsBST tree = new IsBST();
        tree.read();
        if (tree.solve()) {
            System.out.println("CORRECT");
        } else {
            System.out.println("INCORRECT");
        }
    }
}
