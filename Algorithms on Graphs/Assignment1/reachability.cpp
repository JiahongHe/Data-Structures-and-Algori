#include <iostream>
#include <vector>

using namespace std;

class Reachability {
private:
    vector<vector<int> > adj;
    vector<int> reachable;
    
    bool find(vector<int>& vec, int x) {
        for (int i = 0; i < vec.size(); i++) {
            if (x == vec[i]) {
                return true;
            }
        }
        return false;
    }
    
    void DFS(int i) {
        reachable.push_back(i);
        for (auto v: adj[i]) {
            if (find(reachable, v)) {
                continue;
            }
            else {
                DFS(v);
            }
        }
    }
    
public:
    Reachability(vector<vector<int> > &adjcency): adj(adjcency) {}
    
    int reach(int x, int y) {
        reachable.clear();
        DFS(x);
        if (find(reachable, y)) {
            return 1;
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
        adj[y - 1].push_back(x - 1);
    }
    int x, y;
    cin >> x >> y;
    Reachability reach = Reachability(adj);
    cout << reach.reach(x - 1, y - 1) << endl;
}
