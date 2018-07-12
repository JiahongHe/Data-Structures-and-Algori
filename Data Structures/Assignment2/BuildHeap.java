import java.io.*;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.StringTokenizer;

public class BuildHeap {
    private int[] data;
    private List<Swap> swaps;
    
    private FastScanner in;
    private PrintWriter out;
    
    public static void main(String[] args) throws IOException {
        new BuildHeap().solve();
    }
    
    private void readData() throws IOException {
        int n = in.nextInt();
        data = new int[n];
        for (int i = 0; i < n; ++i) {
            data[i] = in.nextInt();
        }
    }
    
    private void writeResponse() {
        out.println(swaps.size());
        for (Swap swap : swaps) {
            out.println(swap.index1 + " " + swap.index2);
        }
    }
    
    private int left_child (int i) {
        return (i * 2 + 1);
    }
    
    public int right_child (int i) {
        return (i * 2 + 2);
    }
    
    public int parent (int i) {
        if (i <= 0) {
            return 0;
        }
        else{
            return ((i - 1) / 2);
        }
    }
    
    public void shift_up(int i) {
        while (i >= 0 && data[parent(i)] > data[i]) {
            swaps.add(new Swap(i, parent(i)));
            int tmp = data[i];
            data[i] = data[parent(i)];
            data[parent(i)] = tmp;
        }
    }
    
    public void shift_down(int i) {
        int r = right_child(i);
        int l = left_child(i);
        int minIndex = i;
        if (r < data.length && data[r] < data[minIndex]) {
            minIndex = r;
        }
        if (l < data.length && data[l] < data[minIndex]) {
            minIndex = l;
        }
        if (i != minIndex) {
            swaps.add(new Swap(i, minIndex));
            int tmp = data[i];
            data[i] = data[minIndex];
            data[minIndex] = tmp;
            shift_down(minIndex);
        }
    }
    
    private void generateSwaps() {
        swaps = new ArrayList<Swap>();
        // The following naive implementation just sorts
        // the given sequence using selection sort algorithm
        // and saves the resulting sequence of swaps.
        // This turns the given array into a heap,
        // but in the worst case gives a quadratic number of swaps.
        //
        // TODO: replace by a more efficient implementation
        int N = data.length;
        for (int i = (N / 2); i >= 0; i--) {
            shift_down(i);
        }
    }
    
    public void solve() throws IOException {
        in = new FastScanner();
        out = new PrintWriter(new BufferedOutputStream(System.out));
        readData();
        generateSwaps();
        writeResponse();
        out.close();
    }
    
    static class Swap {
        int index1;
        int index2;
        
        public Swap(int index1, int index2) {
            this.index1 = index1;
            this.index2 = index2;
        }
    }
    
    static class FastScanner {
        private BufferedReader reader;
        private StringTokenizer tokenizer;
        
        public FastScanner() {
            reader = new BufferedReader(new InputStreamReader(System.in));
            tokenizer = null;
        }
        
        public String next() throws IOException {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                tokenizer = new StringTokenizer(reader.readLine());
            }
            return tokenizer.nextToken();
        }
        
        public int nextInt() throws IOException {
            return Integer.parseInt(next());
        }
    }
}
