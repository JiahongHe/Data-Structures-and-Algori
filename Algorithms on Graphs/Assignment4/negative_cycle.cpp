#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Graph {
private:
    vector<vector<int> > adj;
    vector<vector<int> > cost;
    vector<int> distance;
    vector<int> prev;
    
    int find_index(vector<int>& vec, int i) {
        vector<int>::iterator ind_itr = find(vec.begin(), vec.end(), i);
        int ind = (int)(ind_itr - vec.begin());
        return ind;
    }
    
    void relax(int u, int v) {
        int ind = find_index(adj[u], v);
        if (distance[v] > distance[u] + cost[u][ind]) {
            distance[v] = distance[u] + cost[u][ind];
            prev[v] = u;
        }
    }
    
    int bellman_ford(int s) {
        bool flag = 0;
        distance[s] = 0;
        for (int j = 0; j < adj.size() - 1; j++) {
            for (int i = 0; i < adj.size(); i++) {
                for (int v: adj[i]) {
                    relax(i, v);
                }
            }
        }
        for (int i = 0; i < adj.size(); i++) {
            for (int v:adj[i]) {
                int ind = find_index(adj[i], v);
                if (distance[v] > distance[i] + cost[i][ind]) {
                    distance[v] = distance[i] + cost[i][ind];
                    prev[v] = i;
                    flag = 1;
                }
            }
        }
        return flag;
    }
    
public:
    Graph(vector<vector<int> > &adj_, vector<vector<int> > &cost_):
    adj(adj_),
    cost(cost_),
    prev(vector<int>(adj_.size(), -1)),
    distance(vector<int>(adj_.size(), numeric_limits<int>::infinity()))
    {}
    
    int negative_cycle() {
        int flag = bellman_ford(0);
        return flag;
    }
};

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int> > adj(n, vector<int>());
    vector<vector<int> > cost(n, vector<int>());
    for (int i = 0; i < m; i++) {
        int x, y, w;
        cin >> x >> y >> w;
        adj[x - 1].push_back(y - 1);
        cost[x - 1].push_back(w);
    }
    Graph g = Graph(adj, cost);
    cout << g.negative_cycle();
}
