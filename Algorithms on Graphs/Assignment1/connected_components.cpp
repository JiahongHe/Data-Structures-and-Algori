#include <iostream>
#include <vector>

using namespace std;

class Graph {
private:
    vector<int> reachable;
    vector<int> visited;
    vector<vector<int>> connected;
    vector<vector<int>> adj;
    bool find(vector<int> vec, int x) {
        for (int i = 0; i < vec.size(); i++) {
            if (x == vec[i]) {
                return true;
            }
        }
        return false;
    }
    void DFS(int i) {
        visited.push_back(i);
        reachable.push_back(i);
        for (int v: adj[i]) {
            if (!find(visited, v)) {
                DFS(v);
            }
        }
    }
    
    vector<int> connected_group(int i) {
        reachable.clear();
        DFS(i);
        return reachable;
    }
    
    vector<vector<int>> find_connected_groups() {
        connected.clear();
        int num_v = (int)adj.size();
        for (int i = 0; i < num_v; i++) {
            if (!find(visited, i)) {
                connected.push_back(connected_group(i));
            }
        }
        return connected;
    }
    
public:
    Graph(vector<vector<int> > &adj_): adj(adj_) {}
    int connected_components() {
        connected.clear();
        find_connected_groups();
        int size = (int)connected.size();
        return size;
    }
};

int main() {
    size_t n, m;
    cin >> n >> m;
    vector<vector<int> > adj(n, vector<int>());
    for (size_t i = 0; i < m; i++) {
        int x, y;
        std::cin >> x >> y;
        adj[x - 1].push_back(y - 1);
        adj[y - 1].push_back(x - 1);
    }
    Graph g = Graph(adj);
    cout << g.connected_components() << endl;
}
