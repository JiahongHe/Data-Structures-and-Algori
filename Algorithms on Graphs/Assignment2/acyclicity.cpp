#include <iostream>
#include <vector>

using namespace std;

class Graph {
    private:
    vector<vector<int>> adj;
    vector<int> visited;
    bool flag;
    
    void DFS(int i) {
        if (!flag) {
            visited[i] = 0;
            for (int v: adj[i]) {
                if (visited[v] == -1) {
                    DFS(v);
                    visited[v] = 1;
                }
                if (visited[v] == 0) {
                    flag = true;
                }
            }
        }
    }
    
    
    public:
    Graph(vector<vector<int>> adj_): adj(adj_), flag(false) {}
    int acylic() {
        for (int i = 0; i < adj.size(); i++) {
            visited = vector<int>((int)adj.size(), -1);
            DFS(i);
            if (flag) {
                return 1;
            }
        }
        return 0;
    }
};

int main() {
    size_t n, m;
    cin >> n >> m;
    vector<vector<int> > adj(n, vector<int>());
    for (size_t i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        adj[x - 1].push_back(y - 1);
    }
    Graph g = Graph(adj);
    cout << g.acylic() << endl;
}

