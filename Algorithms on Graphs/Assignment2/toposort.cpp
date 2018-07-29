#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Graph {
private:
    vector<int> visited;
    vector<vector<int>> adj;
    vector<int> topnum;
    int num;
    
    void DFS(int i) {
        visited[i] = 0;
        for (int v: adj[i]) {
            if (visited[v] == -1) {
                DFS(v);
            }
        }
        topnum[i] = num;
        num -= 1;
    }
    
public:
    Graph(vector<vector<int>>& adj_):
    adj(adj_),
    num((int)adj_.size()),
    topnum(vector<int>(adj_.size(), -1))
    {}
    
    vector<int> toposort(vector<vector<int> > adj) {
        vector<int> toposorted;
        visited = vector<int>(adj.size(), -1);
        for (int i = 0; i < adj.size(); i++) {
            if (visited[i] == -1) {
                DFS(i);
            }
        }
        vector<int> order = vector<int>(topnum.size(), -1);
        for (int i = 0; i < topnum.size(); i++) {
            order[topnum[i]-1] = i;
        }
        return order;
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
    vector<int> order = g.toposort(adj);
    for (size_t i = 0; i < order.size(); i++) {
        cout << order[i] + 1 << " ";
    }
}
