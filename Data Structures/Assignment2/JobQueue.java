import java.io.*;
import java.util.Comparator;
import java.util.StringTokenizer;
import java.util.PriorityQueue;

public class JobQueue {
    private int numWorkers;
    private int[] jobs;
    
    private int[] assignedWorker;
    private long[] startTime;
    
    private FastScanner in;
    private PrintWriter out;
    
    public static void main(String[] args) throws IOException {
        new JobQueue().solve();
    }
    
    private class Worker {
        public int id;
        public long nextFreeTime;
        public Worker(int i) {
            id = i;
            nextFreeTime = 0;
        }
        public int getId() {return id;}
        public long getTime() {return nextFreeTime;}
    }
    
    private void readData() throws IOException {
        numWorkers = in.nextInt();
        int m = in.nextInt();
        jobs = new int[m];
        for (int i = 0; i < m; ++i) {
            jobs[i] = in.nextInt();
        }
    }
    
    private void writeResponse() {
        for (int i = 0; i < jobs.length; ++i) {
            out.println(assignedWorker[i] + " " + startTime[i]);
        }
    }
    
    private void assignJobs() {
        assignedWorker = new int[jobs.length];
        startTime = new long[jobs.length];
        PriorityQueue<Worker> queue = new PriorityQueue<Worker>(new Comparator<Worker>() {
            @Override
            public int compare(Worker o1, Worker o2) {
                if (o1.nextFreeTime == o2.nextFreeTime) { return o1.id - o2.id; }
                else { return Integer.parseInt(String.valueOf(o1.nextFreeTime - o2.nextFreeTime)); }
            }
        });
        for (int i = 0; i < numWorkers; ++i) {
            queue.add(new Worker(i));
        }
        for (int i = 0; i < jobs.length; ++i) {
            Worker worker = queue.peek();
            queue.poll();
            assignedWorker[i] = worker.id;
            startTime[i] = worker.nextFreeTime;
            worker.nextFreeTime += jobs[i];
            queue.add(worker);
        }
    }
    
    public void solve() throws IOException {
        in = new FastScanner();
        out = new PrintWriter(new BufferedOutputStream(System.out));
        readData();
        assignJobs();
        writeResponse();
        out.close();
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
