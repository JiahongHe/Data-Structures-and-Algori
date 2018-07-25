import java.util.*;
import java.io.*;

public class tree_orders {
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
    
    public class TreeOrders {
        int n;
        int[] key, left, right;
        ArrayList<Integer> result = new ArrayList<Integer>();
        
        void read() throws IOException {
            FastScanner in = new FastScanner();
            n = in.nextInt();
            key = new int[n];
            left = new int[n];
            right = new int[n];
            
            for (int i = 0; i < n; i++) {
                key[i] = in.nextInt();
                left[i] = in.nextInt();
                right[i] = in.nextInt();
            }
        }
        
        void inOrderTraverse(int i) {
            if (left[i] != -1) {
                inOrderTraverse(left[i]);
            }
            result.add(key[i]);
            if (right[i] != -1) {
                inOrderTraverse(right[i]);
            }
        }
        
        void preOrderTraverse(int i) {
            result.add(key[i]);
            if (left[i] != -1) {
                preOrderTraverse(left[i]);
            }
            if (right[i] != -1) {
                preOrderTraverse(right[i]);
            }
        }
        
        void postOrderTraverse(int i) {
            if (left[i] != -1) {
                postOrderTraverse(left[i]);
            }
            if (right[i] != -1) {
                postOrderTraverse(right[i]);
            }
            result.add(key[i]);
        }
        
        List<Integer> inOrder() {
            result.clear();
            inOrderTraverse(0);
            return result;
        }
        
        List<Integer> preOrder() {
            result.clear();
            preOrderTraverse(0);
            return result;
        }
        
        List<Integer> postOrder() {
            result.clear();
            postOrderTraverse(0);
            return result;
        }
    }
    
    static public void main(String[] args) throws IOException {
        new Thread(null, new Runnable() {
            public void run() {
                try {
                    new tree_orders().run();
                } catch (IOException e) {
                }
            }
        }, "1", 1 << 26).start();
    }
    
    public void print(List<Integer> x) {
        for (Integer a : x) {
            System.out.print(a + " ");
        }
        System.out.println();
    }
    
    public void run() throws IOException {
        TreeOrders tree = new TreeOrders();
        tree.read();
        print(tree.inOrder());
        print(tree.preOrder());
        print(tree.postOrder());
    }
}
