import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;

public class Trie {
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
    
    ArrayList<HashMap<Character, Integer>> buildTrie(String[] patterns) {
        ArrayList<HashMap<Character, Integer>> trie = new ArrayList<HashMap<Character, Integer>>();
        trie.add(new HashMap<Character, Integer>());
        int node_count = 1;
        for (String pattern: patterns) {
            int curr_node = 0;
            for (int i = 0; i < pattern.length(); i++) {
                char c = pattern.charAt(i);
                if (!trie.get(curr_node).containsKey(c)) {
                    trie.get(curr_node).put(c, node_count);
                    trie.add(new HashMap<Character, Integer>());
                    node_count++;
                }
                curr_node = trie.get(curr_node).get(c);
            }
        }
        return trie;
    }
    
    static public void main(String[] args) throws IOException {
        new Trie().run();
    }
    
    public void print(ArrayList<HashMap<Character, Integer>> trie) {
        for (int i = 0; i < trie.size(); ++i) {
            HashMap<Character, Integer> node = trie.get(i);
            for (HashMap.Entry<Character, Integer> entry : node.entrySet()) {
                System.out.println(i + "->" + entry.getValue() + ":" + entry.getKey());
            }
        }
    }
    
    public void run() throws IOException {
        FastScanner scanner = new FastScanner();
        int patternsCount = scanner.nextInt();
        String[] patterns = new String[patternsCount];
        for (int i = 0; i < patternsCount; ++i) {
            patterns[i] = scanner.next();
        }
        ArrayList<HashMap<Character, Integer>> trie = buildTrie(patterns);
        print(trie);
    }
}
